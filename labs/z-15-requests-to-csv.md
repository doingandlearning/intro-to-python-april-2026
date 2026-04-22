# Lab 15: Fetch Data with Requests and Save to CSV

This lab focuses on retrieving API data with `requests` and writing selected results to CSV.

You will practise:

- sending HTTP `GET` requests
- checking response status codes
- parsing JSON responses
- extracting only useful fields
- writing structured output with `csv.writer`

---

## Hints and Tips

- Start by printing a small part of the JSON to understand its structure.
- Check `response.status_code` before using response data.
- Keep extraction logic in a separate function.
- Write a CSV header row so the file is readable.
- Save only the fields you need for your analysis.

---

## Task 1: Send a GET Request and Inspect JSON

Use `requests` to fetch data from:

`https://jsonplaceholder.typicode.com/users`

Requirements:

1. Send a `GET` request.
2. Print the status code.
3. Convert to JSON.
4. Print the first user record only.

<details>
<summary>Solution (Task 1)</summary>

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

print("Status:", response.status_code)

users = response.json()
print(users[0])
```

</details>

---

## Task 2: Extract Selected Fields

Write a function:

`extract_user_rows(users)`

Each row should contain:

1. `id`
2. `name`
3. `email`
4. `city` (from `address`)

Return the rows as a list of tuples.

<details>
<summary>Solution (Task 2)</summary>

```python
def extract_user_rows(users):
    rows = []
    for user in users:
        user_id = user["id"]
        name = user["name"]
        email = user["email"]
        city = user["address"]["city"]
        rows.append((user_id, name, email, city))
    return rows
```

</details>

---

## Task 3: Write Extracted Data to CSV

Write a function:

`write_users_csv(filename, rows)`

Requirements:

1. Use `csv.writer`.
2. Write a header row:
   `["id", "name", "email", "city"]`
3. Write one row per user.

<details>
<summary>Solution (Task 3)</summary>

```python
import csv


def write_users_csv(filename, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email", "city"])
        for row in rows:
            writer.writerow(row)
```

</details>

---

## Task 4: Build a Complete Pipeline

Write a script that:

1. fetches users from the API
2. checks for status code `200`
3. extracts user rows
4. writes `users.csv`
5. prints how many rows were written

<details>
<summary>Solution (Task 4)</summary>

```python
import requests
import csv


def extract_user_rows(users):
    rows = []
    for user in users:
        rows.append(
            (
                user["id"],
                user["name"],
                user["email"],
                user["address"]["city"],
            )
        )
    return rows


def write_users_csv(filename, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email", "city"])
        writer.writerows(rows)


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    rows = extract_user_rows(users)
    write_users_csv("users.csv", rows)
    print(f"Wrote {len(rows)} rows to users.csv")
else:
    print(f"Request failed with status code {response.status_code}")
```

</details>

---

## Task 5 (Optional): Filter Before Writing

Add a function:

`filter_by_city(rows, city_name)`

Requirements:

1. Return only rows where city matches `city_name`.
2. Write filtered output to `users_in_city.csv`.
3. Print the number of rows in the filtered file.

<details>
<summary>Solution (Task 5 Optional)</summary>

```python
def filter_by_city(rows, city_name):
    filtered = []
    for row in rows:
        if row[3] == city_name:
            filtered.append(row)
    return filtered


city_rows = filter_by_city(rows, "Gwenborough")
write_users_csv("users_in_city.csv", city_rows)
print(f"Filtered rows: {len(city_rows)}")
```

</details>

---

## Reflection

- Why is it useful to extract selected fields instead of saving the full JSON?
- What checks should happen before writing API data to disk?
- Where did functions make the request-to-CSV workflow cleaner?
