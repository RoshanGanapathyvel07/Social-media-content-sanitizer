# SocialMedia Content Sanitizer

posts = [
    "User123: I hate this platform http://badlink.com",
    "User456: This is a good day!",
    "User123: toxic behavior should stop https://example.com",
    "User789: Nothing bad here"
]

banned_words = ["bad", "toxic", "hate"]

cleaned_posts = []
links = []
user_flags = {}

total_posts = len(posts)
cleaned_count = 0
clean_posts_count = 0

for post in posts:
    words = post.split()
    cleaned_post = post
    flagged = False

    user = post.split(":")[0]

    if user not in user_flags:
        user_flags[user] = 0

    for word in banned_words:
        if word in cleaned_post.lower():
            cleaned_post = cleaned_post.replace(word, "***")
            flagged = True

    for word in words:
        if word.startswith("http"):
            links.append(word)

    if flagged:
        cleaned_count += 1
        user_flags[user] += 1
    else:
        clean_posts_count += 1

    cleaned_posts.append(cleaned_post)

with open("links_found.txt", "w") as f:
    for link in links:
        f.write(link + "\n")

print("Total Posts Screened:", total_posts)
print("Cleaned (Flagged):", cleaned_count)
print("Clean (No Issues):", clean_posts_count)

print("\nUser Report:")
print(user_flags)

print("\nCleaned Posts:")
for p in cleaned_posts:
    print(p)
