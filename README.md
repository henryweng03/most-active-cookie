# most-active-cookie
most-active-cookie is a Python script that determines the most active cookie in a given day from a cookie log sorted by day

## Installation and Setup
1) Clone the repo
  ```sh
  git clone git@github.com:henryweng03/most-active-cookie.git
  ```
2) Open a terminal window in the repo and run (MacOS and Linux only)
  ```sh
  chmod +x most_active_cookie
  ```

## Usage

To run the script, open a terminal window in the repo and run the following:

(MacOS and Linux)
```sh
./most_active_cookie [FILENAME] -d [DATE]
```

(Windows)
```sh
python3 most_active_cookie [FILENAME] -d [DATE]
```

The filename must be a CSV file (include the extension), and the date must be formatted in YYYY-MM-DD.

### Example

Running the following would find the most active cookie in "cookie_log.csv" on 2018-12-09

(MacOS and Linux)
```sh
./most_active_cookie cookie_log.csv -d 2018-12-09
```

(Windows)
```sh
python3 most_active_cookie cookie_log.csv -d 2018-12-09
```
