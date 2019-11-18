from goodreads import client

gc = client.GoodreadsClient("", "")

userid = 33298999
gc.authenticate()
user = gc.user(userid)

shelves = user.shelves()
reviews = user.reviews()
group = user.list_groups()
book = user.owned_books()

print("")

# shelves = user.shelves()
# print(shelves.count)