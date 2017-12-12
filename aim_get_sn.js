// Start by logging in to www.aim.com and zoom way out
usernames = []

// Run this a bunch of times after scrolling a bit to get the next set of screen names
els = document.getElementsByClassName('user-item');
for (var i = 0; i < els.length; i++) {
    console.log(els[i].id);
    usernames.push(els[i].id)
// as you can see modified above portion from ".textContext" to ".id"
}
