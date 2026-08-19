#!/usr/bin/env python3
"""
Comprehensive test suite for deck-presets API
Tests all CRUD operations, edge cases, and cleanup
"""

import requests
import json
import uuid
import sys
from typing import List, Dict, Any

# Base URL from frontend/.env
BASE_URL = "https://design-sprint-aug26.preview.emergentagent.com/api"
FALLBACK_URL = "http://localhost:8001/api"

# Track created preset IDs for cleanup
created_preset_ids: List[str] = []

def test_connection(base_url: str) -> bool:
    """Test if the API is reachable"""
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Connection failed to {base_url}: {e}")
        return False

def get_base_url() -> str:
    """Determine which base URL to use"""
    if test_connection(BASE_URL):
        print(f"✓ Using external URL: {BASE_URL}")
        return BASE_URL
    elif test_connection(FALLBACK_URL):
        print(f"✓ Using fallback URL: {FALLBACK_URL}")
        return FALLBACK_URL
    else:
        print("✗ CRITICAL: Neither external nor fallback URL is reachable")
        sys.exit(1)

def is_valid_uuid(val: str) -> bool:
    """Check if a string is a valid UUID"""
    try:
        uuid.UUID(val)
        return True
    except (ValueError, AttributeError):
        return False

def cleanup_all_presets(base_url: str):
    """Delete all presets created during testing"""
    print("\n" + "="*80)
    print("CLEANUP: Deleting all created presets")
    print("="*80)
    
    for preset_id in created_preset_ids:
        try:
            response = requests.delete(f"{base_url}/presets/{preset_id}", timeout=10)
            if response.status_code == 200:
                result = response.json()
                if result.get("deleted"):
                    print(f"✓ Deleted preset {preset_id}")
                else:
                    print(f"⚠ Preset {preset_id} not found (may have been deleted already)")
            else:
                print(f"✗ Failed to delete preset {preset_id}: HTTP {response.status_code}")
        except Exception as e:
            print(f"✗ Error deleting preset {preset_id}: {e}")
    
    # Verify collection is empty
    try:
        response = requests.get(f"{base_url}/presets", timeout=10)
        if response.status_code == 200:
            presets = response.json()
            if len(presets) == 0:
                print(f"✓ Collection is now empty")
            else:
                print(f"⚠ Collection still has {len(presets)} preset(s)")
    except Exception as e:
        print(f"✗ Error verifying cleanup: {e}")

def run_tests():
    """Run all test scenarios"""
    base_url = get_base_url()
    
    print("\n" + "="*80)
    print("TEST 1: GET /api/ - Verify existing template route still works")
    print("="*80)
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data.get("message") == "Hello World", f"Expected 'Hello World', got {data}"
        print(f"✓ PASS: Template route returns correct message")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 2: GET /api/presets - Initial list (may be empty)")
    print("="*80)
    try:
        response = requests.get(f"{base_url}/presets", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        presets = response.json()
        assert isinstance(presets, list), f"Expected list, got {type(presets)}"
        print(f"✓ PASS: GET /api/presets returns list with {len(presets)} preset(s)")
        initial_count = len(presets)
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 3: POST /api/presets - Create first preset with unicode")
    print("="*80)
    try:
        payload = {
            "name": "Acme Corp",
            "fields": {
                "client": "John",
                "company": "Acme",
                "price-growth": "₹2,00,000"
            }
        }
        response = requests.post(f"{base_url}/presets", json=payload, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        preset = response.json()
        assert "id" in preset, "Response missing 'id' field"
        assert is_valid_uuid(preset["id"]), f"Invalid UUID: {preset['id']}"
        assert preset["name"] == "Acme Corp", f"Name mismatch: {preset['name']}"
        assert preset["fields"] == payload["fields"], f"Fields mismatch: {preset['fields']}"
        assert "updated_at" in preset, "Response missing 'updated_at' field"
        assert "_id" not in preset, "MongoDB _id leaked in response"
        
        # Store for cleanup and later tests
        first_preset_id = preset["id"]
        created_preset_ids.append(first_preset_id)
        
        print(f"✓ PASS: Created preset with id={first_preset_id}")
        print(f"  - Name: {preset['name']}")
        print(f"  - Fields: {preset['fields']}")
        print(f"  - Unicode preserved: {preset['fields']['price-growth']}")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 4: UPSERT-BY-NAME - POST same name with different fields")
    print("="*80)
    try:
        payload = {
            "name": "Acme Corp",
            "fields": {
                "client": "Jane",
                "company": "Acme Industries",
                "price-growth": "₹5,00,000"
            }
        }
        response = requests.post(f"{base_url}/presets", json=payload, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        preset = response.json()
        assert preset["id"] == first_preset_id, f"ID changed! Expected {first_preset_id}, got {preset['id']}"
        assert preset["name"] == "Acme Corp", f"Name mismatch: {preset['name']}"
        assert preset["fields"] == payload["fields"], f"Fields not updated: {preset['fields']}"
        
        print(f"✓ PASS: Upsert kept same id={preset['id']}")
        print(f"  - Fields updated: {preset['fields']}")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 5: Verify list shows only ONE preset with updated fields")
    print("="*80)
    try:
        response = requests.get(f"{base_url}/presets", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        presets = response.json()
        acme_presets = [p for p in presets if p["name"] == "Acme Corp"]
        assert len(acme_presets) == 1, f"Expected 1 'Acme Corp' preset, found {len(acme_presets)}"
        assert acme_presets[0]["fields"]["client"] == "Jane", "Fields not updated in list"
        
        print(f"✓ PASS: List shows only ONE 'Acme Corp' preset with updated fields")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 6: POST second preset with different name")
    print("="*80)
    try:
        payload = {
            "name": "TechStart Inc",
            "fields": {
                "client": "Alice",
                "company": "TechStart",
                "price-growth": "₹10,00,000"
            }
        }
        response = requests.post(f"{base_url}/presets", json=payload, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        preset = response.json()
        assert is_valid_uuid(preset["id"]), f"Invalid UUID: {preset['id']}"
        assert preset["id"] != first_preset_id, "Second preset has same ID as first"
        
        second_preset_id = preset["id"]
        created_preset_ids.append(second_preset_id)
        
        print(f"✓ PASS: Created second preset with id={second_preset_id}")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 7: Verify list contains 2 presets, newest first")
    print("="*80)
    try:
        response = requests.get(f"{base_url}/presets", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        presets = response.json()
        our_presets = [p for p in presets if p["id"] in created_preset_ids]
        assert len(our_presets) == 2, f"Expected 2 presets, found {len(our_presets)}"
        
        # Check sorting (newest first)
        if len(presets) >= 2:
            first_time = presets[0]["updated_at"]
            second_time = presets[1]["updated_at"]
            # TechStart should be first (newest)
            assert presets[0]["name"] == "TechStart Inc", f"Expected newest first, got {presets[0]['name']}"
        
        print(f"✓ PASS: List contains 2 presets, sorted by updated_at desc")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 8: Edge case - POST with whitespace-only name")
    print("="*80)
    try:
        payload = {
            "name": "   ",
            "fields": {"test": "value"}
        }
        response = requests.post(f"{base_url}/presets", json=payload, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        preset = response.json()
        assert preset["name"] == "Untitled Client", f"Expected 'Untitled Client', got '{preset['name']}'"
        
        whitespace_preset_id = preset["id"]
        created_preset_ids.append(whitespace_preset_id)
        
        print(f"✓ PASS: Whitespace-only name converted to 'Untitled Client'")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 9: Edge case - POST with 100-char name (should truncate to 60)")
    print("="*80)
    try:
        long_name = "A" * 100
        payload = {
            "name": long_name,
            "fields": {"test": "value"}
        }
        response = requests.post(f"{base_url}/presets", json=payload, timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        preset = response.json()
        assert len(preset["name"]) == 60, f"Expected 60 chars, got {len(preset['name'])}"
        assert preset["name"] == "A" * 60, f"Name not truncated correctly"
        
        long_preset_id = preset["id"]
        created_preset_ids.append(long_preset_id)
        
        print(f"✓ PASS: 100-char name truncated to 60 chars")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 10: DELETE with real id")
    print("="*80)
    try:
        # Delete the first preset
        response = requests.delete(f"{base_url}/presets/{first_preset_id}", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        result = response.json()
        assert result.get("deleted") == True, f"Expected deleted=true, got {result}"
        
        # Verify it's gone from the list
        response = requests.get(f"{base_url}/presets", timeout=10)
        presets = response.json()
        deleted_preset = [p for p in presets if p["id"] == first_preset_id]
        assert len(deleted_preset) == 0, "Deleted preset still in list"
        
        # Remove from cleanup list since it's already deleted
        created_preset_ids.remove(first_preset_id)
        
        print(f"✓ PASS: Preset deleted successfully and removed from list")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 11: DELETE with random UUID (should return deleted=false, not 500)")
    print("="*80)
    try:
        random_uuid = str(uuid.uuid4())
        response = requests.delete(f"{base_url}/presets/{random_uuid}", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        result = response.json()
        assert result.get("deleted") == False, f"Expected deleted=false, got {result}"
        
        print(f"✓ PASS: DELETE with unknown UUID returns deleted=false (not 500)")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    print("\n" + "="*80)
    print("TEST 12: Verify no MongoDB _id leaks in any response")
    print("="*80)
    try:
        response = requests.get(f"{base_url}/presets", timeout=10)
        presets = response.json()
        
        for preset in presets:
            assert "_id" not in preset, f"MongoDB _id leaked in preset: {preset}"
        
        print(f"✓ PASS: No MongoDB _id found in any response")
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False
    
    # Cleanup
    cleanup_all_presets(base_url)
    
    print("\n" + "="*80)
    print("ALL TESTS PASSED ✓")
    print("="*80)
    return True

if __name__ == "__main__":
    try:
        success = run_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
