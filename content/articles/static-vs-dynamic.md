Title: Why I chose Pelican and how I update blog posts
Date: 2019-05-13 
Category: General
Tags: Python, Pelican, Blogging
Slug: pelican-sites-and-creating-blogposts
Authors: Adriana
Summary: The advantages of a static site, and a brief tutorial how I create blog posts.
Status: published

I've explored creating all kinds of websites.  

It began years ago with a Geocities site (!!) that I made when I had my wisdom teeth pulled and I didn't want to leave my room. Since then, I've created sites using: Tumbler, Blogger, Wordpress, HuGo, Squarespace, a Pelican-generated site and a Python-Django site. I'm sure I've left some out. 

I am by no means an expert. Until recently, it's been more of a light hobby than a necessity. 

Eventually, I needed something for my [consulting business](www.dranalytics.co) and I now I've gone the personal route because it didn't seem appropriate to write about making lemon curd alongside recent news on DNA sequence alignment software.

For my company I chose squarespace, which is just lovely and easy to set up.

I chose to go with Pelican for my personal blog because:

1. I love Python;
2. a static site seems appropriate for just linking to recent projects, book lists, and random thoughts (no complex user interfaces, no databases....yet); 
3. the documentation is pretty substantial (as a relatively new coder, this is essential);
4. and unlike my company website, I wanted to build something from scratch.

### The Gist of Pelican

Pelican is, by definition, a static site generator. In a nutshell, what this means is that webpages are generated on my computer, pushed to a server, and then presented when accessed by someone on the internet. 

In contrast, a dynamic website has pages that are created in real-time as it is accessed by the user. This can include drawing data from a database, logging into apps, amongst other things. 

### How I use Pelican

I have a folder that contains my content in the form of either markdown or html. Whenever I want to add a blog post, I start a new markdown file, add the necessary metadata, and start writing. 

Then I perform these commands to update my website, which is hosted by Github User pages.

First, I save my changes to my 'source branch'.

	
```
$git add .
# stages the current changes for a commit
    
$git commit -a -m "blog update"
# commits the all the changes to my local repository, with a message of 'blog update'
    
$git push
# submits these committed changes to the remote repository
```	


Since user pages only deploy from the 'master' branch in your repository, you can just push your source's 'output' folder to the master branch and your blog will be updated. A way to do this is:

```
$pelican content -o output -s pelicanconf.py
# uses the pelican command with path to content ('content' here), to an output
# folder of 'output', using settings file 'pelicanconf.py'
    
$ghp-import output -r origin -b master
# githubpages import will update the master branch with contents of output 
# from the remote origin
    
$git push origin master
# updates the the remote master branch, publishing the site
```

Sources:

[https://docs.getpelican.com/en/4.0.1/tips.html](https://docs.getpelican.com/en/4.0.1/tips.html)

[http://ndpsoftware.com/git-cheatsheet.html#loc=workspace;](http://ndpsoftware.com/git-cheatsheet.html#loc=workspace;) 

