#Wordpress 3: Plugins, CSS, SEO and Analytics
*(Customizing your site, and getting feedback)*

You can find the link to this Handout on the Digital Fellows >> Resources >> Handouts Tab

Plugins to Install onto your Academic Commons Site for use today:
* Wordpress SEO by Yoast
* Google Fonts

If you’re on a personal computer and use Firefox: Download the Firefly plugin to your web browser

By participating in this workshop, you will be able to:
•  Use plugins to add functionality to your site (almost anything you can imagine),
•  Add custom CSS to over-ride the theme defaults, and customize your site, and
•  Install analytics to understand how visitors use your site and the demographics you are reaching.

---

##I. Widgets vs. Plugins

    | Widgets | Plugins
--- | :---: | :---:
Drag & Drop  |  Yes  |  No
Adds functionality for users  |  Yes  |  Yes
Nearly infinite number  |  No  |  Yes

Widgets will show something to your user in one of the designated locations (sidebar, footer, etc.) 
For example, you want to add a 1 sentence description on the far right side about you. This is a text widget in the main (or right) sidebar.

Plugins add functionality to your site and may or may not change the appearance of your site. 
For example, you want to add a fillable contact form to a page. This is a plugin “Contact Form 7”

There are 277 plugins on the Academic Commons. Below is a sampling of some and how they work. Before installing any plugin, be sure to go to the plugin site to find out how it works and to be sure its still being maintained. Even though the AC vets them when they are added, some may become outdated in that time.

##II. Customizing your Site or Blog

1. CSS: Cascading Style Sheets
  a. Wordpress reads this document to tell it how to render the html (you can’t alter the html).
2. What can CSS do??
  1. Change fonts, colors, sizes, etc. of each text type (i.e., paragraphs, headings, subheadings, etc.)
  2. Hide or display fonts
  3. Change backgrounds, add or take away borders, etc.
  4. Change the width of the content area or sidebars
  5. So much more!
3. To change the CSS, go to Appearance  Custom User CSS in the Dashboard menu
4. First example: Hiding the meta data on posts
5. How to do this on any theme
  * footer.entry-meta is called a ‘selector’. It tells the CSS what ‘element’ to modify. This part is theme-specific
  * visibility: hidden  tells it what to do. This is pretty much the same across themes, and is always surrounded by { }
  * visibility is called a ‘property’, hidden is called a ‘value’. Each element has multiple properties. Each property should have only one value.
6. But how do I know what the selector is called on my theme?
  * Option 1: Search for it by typing in the name of your theme and what you want to do http://en.forums.wordpress.com/forum/css-customization
  * Option 2: Use the dev tools
    1. Chrome: go to View  Developer  Developer Tools (on a Mac: alt+command+i)
    2. Firefox: Download Firebug
      * Go to Tools Web Developer  Firebug  Open Firebug
    3. Click on the magnifying glass then highlight the object you want to find the selector for.
      * The element’s selector will appear highlighted in the html in the main window, and at the top of the Style tab of the window on the right. 
      * In the example below, ‘Older Posts’ is highlighted, and corresponds to `.nav-previous`
      * The current properties and values appear in the Style window.
    4. Copy and Paste the selector and all of its properties and values into the Custom User CSS on your dashboard
    5. Change the values to what you want (i.e., change float: left  to float: right)
      * The changes made here will apply to the entire site. 
      * It is possible to make page by page alterations as well. Copy the new CSS you want that page to follow into the top of the page in the text portion of the content window.
7. Now let’s change the font!
  * My favorite way to do this is with the Google Fonts Plugin.
    1. Install Google Fonts
    2. Go to the Google Fonts page and pick a font https://www.google.com/fonts#
    3. Click on “Quick Select” (the second little box)
    4. Copy the CSS code from step 4 (you don’t need to do the other steps if you have installed the Google Fonts Plugin!)
    5. Copy the font name into your Custom CSS with the type of font you want to change

If you want to change a specific piece of text, use these tags around it:

```HTML
<p> blah blah blah </p>
<h1> blah blah blah </h1>
<h2> blah blah blah </h2>
<h3> blah blah blah </h3>
<h4> blah blah blah </h4>
<h5> blah blah blah </h5>
<h6> blah blah blah </h6>
```

Which displays like this:
<p> blah blah blah </p>
<h1> blah blah blah </h1>
<h2> blah blah blah </h2>
<h3> blah blah blah </h3>
<h4> blah blah blah </h4>
<h5> blah blah blah </h5>
<h6> blah blah blah </h6>

Usually use one of the header that you are not likely to use (i.e., h5 or h6)
  
That’s it! If ever in doubt about what values to use, just search for it. If it’s ambiguous, there will be discussion about it on either the Wordpress Codex or Stack exchange (and many other places, too)

---

##III. Search Engine Optimization (SEO)

1. What is SEO? 
  * Search Engines such as Google, Yahoo, Bing, etc. ranks pages based on a variety of metrics based on a proprietary algorithm. Some features of the algorithm are always relevant and never change. Some of the more nuanced items change. 
2. Why should academics care about SEO – we are building our names, not a product!
  * Yes, this is true – but it would be nice for people to find you based on your field, your research interests, or your achievements in addition to your name.
  * Secondly, things like twitter, facebook, etc. have absurdly high SEOs – it would be better to be found for something you intentionally curate. 
3. How do I increase my SEO? 
  * This is definitely a balancing act for academics – some SEO optimization techniques just won’t work for the type of sites we usually build (i.e., resource pages with lots of links), but others will (i.e., good organization, clear writing, and clear meta data).

Let’s start with a simple plugin:
*Wordpress SEO by Yoast*

1. Install the Plugin: Wordpress SEO by Yoast
2. Configure the settings (or leave the defaults) – the Take a Tour button will take you through more than we can get through today.
3. Go to edit any Page or Post on your site to get a summary of the SEO for your site. 
  * At the bottom of the page are the SEO Functions. On the General Tab, there is Snippet Preview (by default this pulls the first few lines from your page – you can change that here in Meta Description).
    * Focus Keyword asks you to set a keyword to summarize your page. Think about who you are trying to attract, and how you would search for your own page. That should be your keyword. 
    * Wordpress SEO uses this to analyze the rest of your page and return suggestions about how to increase your SEO.
    * It will give you further analysis on the Page Analysis tab, graded by how important Wordpress SEO finds the issue to be.

---

##IV. Analytics
1. Google Analytics is definitely the most common Analytics type. Because the Academic Commons is a multi-user installation, you have to request your analytics report from the commons. 
  1. Useful to find out who is accessing your site, how often, and from where. 
  2. If you build something big, this is a great metric to have on a resume (or a really digitally oriented CV).
2. Another option is clicky analytics http://clicky.com/ this is free, and the code they provide you with can just be copy and pasted into your pages – but there will be a button indicating that clicky analytics are tracking your site.
3. To set up clicky analytics: 
  1. Create a login, it will take you to a page similar to this: From here, Add New Site
  2. Put in the url for a site you own
  3. Pick up the tracking code
  4. Copy the code in red here (if you’re nervous about the copy-paste, put it into a txt document to hold onto it)
  5. Go back to the Edit Page mode of your Academic Commons Site in the Text Tab, put the script at the bottom of the page
    * Personally, I go back to the Visual tab and make all the text white (cause it matches my background) – the button will still appear, just not the text.
  6. Then, go back to the clicky website and you’ll see who has visited your site!

---

##V. Questions?

Thank you!  Best of luck customizing your site!
Please take a moment to give us some feedback here: http://digitalfellows.commons.gc.cuny.edu/workshopevaluationform/

