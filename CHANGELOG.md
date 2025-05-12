# 📦 Samaaja Changelog

## 🚀 Version 15 - Released on May 12, 2025

### 🆕 New Features

- **User Metadata Doctype**: Introduced a new doctype `User Metadata` to store additional user profile details like `age`, `city`, `state`, `org_id`, `verified_by`, etc.
- **Profile Enhancements**: Improved profile view and logic to incorporate extended metadata cleanly.
- **Patch Scripts**:
  - `create_user_metadata_for_existing_users.py`: Backfills metadata for existing users.
  - `update_user_bio_from_headline.py`: Sets `bio` from `headline` if missing.

### ♻️ Refactoring & Renaming

- **Asset Doctype Refactoring**:
  - `Asset` → `Samaaja Asset`
  - `Asset Category` → `Samaaja Asset Category`
  - `Asset Status` → `Samaaja Asset Status`
  - `Asset Sub Category` → `Samaaja Asset Sub Category`
  - `Asset Type` → `Samaaja Asset Type`
- All related Python modules, test files, and client-side JS were renamed and updated.

### 📅 Event Module Enhancements

- Updated schemas, form layouts, and list views for:
  - `Event Category`
  - `Event Source`
  - `Event Status`
  - `Event Sub Category`
  - `Event Type`
  - `Events`
- These changes improve consistency and usability in the Desk UI.

### 📊 Performance & Backend Improvements

- Refined statistical query logic in `www/stats/index.py` for faster and cleaner aggregation.
- Updated backend logic in:
  - `api/action.py`
  - `api/common.py`
  - `api/location.py`
  - `overrides/user.py`

### 🧩 Hooks & Integration

- Updated `hooks.py` to register new doctypes and patch files.
- Ensured seamless integration of overrides and new features.

---

**Commit:** [`4866922`](https://github.com/fossunited/Samaaja/commit/48669226cb7254fe0c175302b685a91f6f272e67)  
**Author:** Anupam Kumar  
**Date:** May 12, 2025  
