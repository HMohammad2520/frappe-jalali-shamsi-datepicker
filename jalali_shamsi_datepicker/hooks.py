app_name = "jalali_shamsi_datepicker"
app_title = "Jalali Shamsi Datepicker"
app_publisher = "Ideenemium"
app_description = "The best solution to change date and datetime fields to Shamsi(Jalali) Calendar."
app_email = "ideenemium@gmail.com"
app_license = "mit"

# jalali_shamsi_datepicker/hooks.py
fixtures = [
    {"doctype": "Custom Field", "filters": {"module": "Jalali Shamsi Datepicker"}}
]

app_include_css = [
    "/assets/jalali_shamsi_datepicker/css/custom.css",
    "/assets/jalali_shamsi_datepicker/css/persian-datepicker.min.css",
]
app_include_js = [
    "/assets/jalali_shamsi_datepicker/js/persian-date-handler.js",
    "/assets/jalali_shamsi_datepicker/js/persian-date.min.js",
    "/assets/jalali_shamsi_datepicker/js/persian-datepicker.min.js",
]