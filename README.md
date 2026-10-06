# CodeBook: Data Cleaning and Recommendation Engine in Pure Python

A mini data science project built for **CodeBook**, a fictional social network for coders. It loads and cleans raw user data, then powers two recommendation features: **People You May Know** and **Pages You Might Like**.

Built with **only Python's standard library**: no pandas, no NumPy, no external packages. I built it right after finishing Python fundamentals, to practise core data structures (lists, sets, dictionaries) on a real-style problem.

---

## Features

### 1. Load and Explore Data
- Reads user and page data from a JSON file using the built-in `json` module
- Prints users, their friend connections, liked pages, and the list of available pages

### 2. Clean and Structure Data
Fixes common data-quality problems:
- Removes users with missing or empty names
- Removes duplicate friend entries
- Removes inactive users (no friends and no liked pages)
- Deduplicates pages by ID

### 3. People You May Know
- Finds friends-of-friends who are not already direct friends
- Ranks suggestions by the **number of mutual friends** (more mutual friends = higher priority)

### 4. Pages You Might Like
- Uses a basic form of **collaborative filtering**: if two users like the same pages, pages liked by one are recommended to the other
- Ranks suggestions by a similarity score (number of pages both users like)

---

## Project Structure

```
Social_network_recommender/
├── codebook_data.json            # Raw input data
├── cleaned_codebook_data.json    # Output after cleaning
├── load_data.py                  # Load and display data
├── clean_data.py                 # Data cleaning
├── people_you_may_know.py        # Friend recommendations
├── pages_you_might_like.py       # Page recommendations
└── README.md
```

> Rename the files above to match your own repo.

---

## How to Run

**Requirements:** Python 3.8+ (no extra installs needed)

```bash
# 1. Clone the repo
git clone https://github.com/Ashwanisinghchouhan1/Social_network_recommender.git
cd Social_network_recommender

# 2. Display the raw data
python load_data.py

# 3. Clean the data (creates cleaned_codebook_data.json)
python clean_data.py

# 4. Get friend recommendations
python people_you_may_know.py

# 5. Get page recommendations
python pages_you_might_like.py
```

---

## Sample Output

**Load and display**
```
Users and Their Connections:

Amit (ID: 1) - Friends: [2, 3] - Liked Pages: [101]
Priya (ID: 2) - Friends: [1, 4] - Liked Pages: [102]
Rahul (ID: 3) - Friends: [1] - Liked Pages: [101, 103]
Sara (ID: 4) - Friends: [2] - Liked Pages: [104]

Pages:

101: Python Developers
102: Data Science Enthusiasts
103: AI & ML Community
104: Web Dev Hub
```

**People You May Know**
```
People You May Know for User 1: [4]
```

**Pages You Might Like**
```
Pages You Might Like for User 1: [103]
```

---

## How the Algorithms Work

**People You May Know**
1. Build a map of each user to their set of friends.
2. For every friend of the target user, look at that friend's friends.
3. Skip the user themselves and anyone already a direct friend.
4. Count how many times each candidate appears (= number of mutual friends).
5. Sort candidates by that count, highest first.

**Pages You Might Like**
1. Build a map of each user to the set of pages they like.
2. For every other user, compute the overlap with the target user's liked pages.
3. Score each page that the target user has not liked using that overlap.
4. Sort pages by score, highest first.

---

## What I Learned
- Working with JSON in Python using `json.load` and `json.dump`
- Cleaning messy data with list comprehensions, sets, and dictionaries
- Using sets for fast lookups and deduplication
- The basic idea behind recommendation systems (mutual connections and collaborative filtering)

## Possible Improvements
- Only score pages from users who share at least one liked page with the target user
- Test on a larger, randomly generated dataset
- Add unit tests
- Expose the recommendations through a simple API

---

## Author
**Ashwani Singh Chouhan**
[GitHub](https://github.com/Ashwanisinghchouhan1)
