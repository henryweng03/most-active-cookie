# most-active-cookie
most-active-cookie is a Python script that determines the most active cookie in a given day from a cookie log sorted by day

## Installation
Clone the repo
```sh
git clone git@github.com:henryweng03/most-active-cookie.git
```

## Usage
To run the script, open a terminal window in the repo and run
```sh
python3 most_active_cookie.py [FILENAME] -d [DATE]
```
The filename must be a CSV file (include the extension), and the date must be formatted in YYYY-MM-DD.

### Example

Running the following would find the most active cookie in "cookie_log.csv" on 2018-12-09
```sh
python3 most_active_cookie.py cookie_log.csv -d 2018-12-09
```
