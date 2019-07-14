Title: Tasty Pastry is live
Date: 2019-07-14 
Category: General
Tags: Python, Django, Tasty Pastry
Slug: tasty-pastry-live
Authors: Adriana
Summary: Some background machanics of how I use heroku for my django app
Status: published

I've hit another milestone and finally made my website live. After weeks of figuring out how I want to present my recipes, and what my plans are for the site, it was finally ready to push out to the production server. 

I've learned quite a bit along the way, and though most of it is specific to django app development (which I believe I have just scratched the surface) I try to make some abstract observations about processes and learning in general. It is my way of making connections between topics and possibly apply ideas across disciplines. I find I can learn many things this way.

That's not to say that I am quick at learning. That is farther from the truth. But, I do believe that I have a higher tolerance for learning new things, in that I will easily pick up many things up at once and try lots of things to figure out what I like. 

Anyway. The main theme that keeps running through my mind as I attempt to learn django/python/app development, is this: 
	
	1. Make it work
	2. Make it fast
	3. Make it simple
(from [the Biostar Handbook](https://www.biostarhandbook.com/index.html) and bioinformatics pipelines)

I think #1 is the most difficult hurdle to overcome and is often where most people (including myself) give up. 

But I love the way that the biostarhandbook describes #1:
	
>"...get the entire process moving - not just the beginning - the whole thing. It will be hacky, it will be squeaky, it may need to be held together with duct tape. Go all the way!"

Because of this, every project that I think about putting together something, even if it is held together by duct tape. (Quite literally - I put together a drip irrigation setup for my garden and the inital pvc piping was indeed held together by duct tape.)

I think it's so tempting to want something polished, finished and beautiful at the getgo, but how many times is ever possible?

So the site is up. There is duct tape remaining on some parts, but it's up. 

Onwards and upwards to #2 (make it fast) and #3 (make it simple).

---

What I'm really digging about app development are all the checkpoints. The scientist in me is appreciating that there are different stages of development to prevent and debug errors. (If only bench research had this sort of feature...)

You have various environments to run your app before it becomes live. First, locally on your machine, then onto a staging environment online, and then onto your production, or live site. Within each of these steps you can add even more checkpoints, like branches using git on your local environment. 

It took some time for me to learn the commands and general workarounds, but I have a somewhat good understanding. At least, enough to go back and fix things if I break something on the app. 

Here is my pipeline on how I push to heroku using git:

1. Verify that all pages are presenting correctly. Click on the recently updated pages to make sure there are no errors.


2. Check to see if the site is mobile friendly:
	
	`python3 manage.py runserver 0.0.0.0:8000` allows you to access the site on your network, check your computer's IP


3. Prepare your static files for deployment
	
	`python3 manage.py collectstatic`


4. Commit all changes to your working branch, pushing to master if needed.


5. Using heroku CLI, you can check to see what apps you have (sometimes I forget what I named them)
	
	`heroku apps`


6. Push to heroku's branch your latest commits. For instance, I named my remote heroku branch for staging "staging", and I have all my recent changes commited to my master.
	
	`git push staging master`


7. When (there is never an 'if') there are errors
	
	`heroku log --tail --remote staging`
	If however this is not helpful, you can try logentries (info from [this stackoverflow answer](https://stackoverflow.com/questions/19410811/how-do-you-diagnose-a-500-error-on-heroku-when-there-is-no-error-message-in-the)).
	This helps me diagnose by giving more details on my errors.


8. If the staging looks good, you can push your commits to the live server, which is called "prod" in my case:
	
	`git push prod master`



[Updates](https://www.tastypastry.kitchen/) are now live! Onto the next issue...









