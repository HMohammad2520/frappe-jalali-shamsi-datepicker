# My App - Persian/Jalali Datepicker for Frappe

A simple Frappe app that integrates a Persian (Jalali) datepicker for **Date** and **Datetime** fields.  
It displays dates in Jalali format for users but stores them in **Gregorian format** in Frappe models.

## Features

- Jalali (Persian) datepicker for `Date` and `Datetime` fields
- Converts Persian dates to Gregorian for database storage
- Shows Gregorian equivalent next to Date fields
- Works with standard Frappe forms
- Includes automatic cleanup of "Only" / "فقط" suffix in `in_words` fields

## Installation

```bash
# Get the app
bench get-app https://github.com/nidyasoft/jalali_shamsi_datepicker

# Install on your site
bench --site yoursite install-app jalali_shamsi_datepicker

# Restart the site
bench --site yoursite restart
```

## Usage

* After installation, New field will be added in `System Settings` for enabling **jalali-datepicker**.
* This app automatically attaches to all **Date** and **Datetime** fields on form load.
* Persian dates are displayed to users, Gregorian dates are saved in the backend.

## Note

To ensure proper functionality, make sure the **Date Format** in Frappe **System Settings** matches the datepicker format (`YYYY/MM/DD`).  
Incorrect formats (like `YYYY/DD/MM`) may cause issues when manually entering dates.

## License

MIT
