# Photography Blog
For my fourth Portfolio Project I have decided to create a photography blog, with the purpose of the site being to provide a space for amateur photographers to showcase thier work, away from the noise of social media.

[Please view the live project here!] (https://pp4-photography-blog-dfac9ff0d622.herokuapp.com/)

## User Experience (UX)
### User Stories
----------------------------
#### First Time Visitor Goals
- As a first time visitor, I want to easily be able to perceive the purpose of the site.
- As a first time visitor, I want to have a positive emotional reaction to the site design.
- As a first time visitor, I want to be able navigate the site intuitively.
- As a first time visitor, I want all of the above to be true, regardless of screen size.
#### Returning Visitor Goals
- As a returning time visitor, I want to be able to view the conversations through the comments that are happening underneath the posts.
- As a returning visitor, I want to easily find the page or section that I am looking for.
#### Frequent Visitor Goals
- As a frequent visitor, I want to be able to easily discern the post authors from one another so that I may find the user whom's style I enjoy.
- As a frequent visitor, I want to easily be able to sign up to use the site's full list of features.
#### Verified User Goals
- As a verified user, I want to easily be able to comment on a post.
- As a verified user, I want easily be able to remove a comment I have made.
- As a verified user, I want to be able to upload a post and join the community.
- As a verified user, I want to be able to amend the post for any errors or mistakes.
- As a verified user, I want to easily be able to remove a post if I so choose.
- As a verified user, I want my posts and my comments to be editable or deletable, only by me and site admins.
- As a verified user, I want to log in and log out of the site with ease.

### Features
----------------------------
#### Existing Features
##### Header
- The header element is identical across all pages of the site. 
- It contains a heading element that acts as the site title and an anchor back to the homepage. This is on the left hand side of the header.
- It also contains a navigation menu to all three pages of the site with the current page the user is on underlined. This is on the right hand side of the header.
#### Hero Image
- The Hero Image, replicated along all pages of the site, depicts photography in action. 
- The header and the subheading overlay the hero image and are also replicated on all site pages
#### index.html
- The site hompage, rendered by the 'index.html' template, contains three sections. 
- The first section shows the three most liked posts on the site at the current time. Here, each post contains the post title, post author, a reduced size version of the post image, the authors caption to the post, how many likes each post has received, along with the location and upload timestamp. All information here is populated my Django from the Post model.
- The second section shows a list of site admins, each with a picture, thier name and a short message for the user. The list is displayed as blocks and is populated by Django from the Editor model.
- The final section of the homepage is a call to action for both verified and non-verified users. If the user is verified, a button will be present to take the user to the AddPost form on 'add_post.html'. If the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'.
#### blog.html
- This page will be populated with every row in the Post model by Django, in order of date created, newer posts appearing at the top.
- Said blog posts will sit inline in rows off three, with any incomplete rows being centered. These blog thumnails contain all the same information as on index.html, but each takes up a smaller section of the page, given that there is far more of them here.
- Just like on index.html, the final section of the blog page is a call to action for both verified and non-verified users. If the user is verified, a button will be present to take the user to the AddPost form on 'add_post.html'. If the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'.
#### specific_post.html
- Here we come to the main purpose of the site, a display of a singluar blog post but a single user. All of the same information is provided as in index.html and blog.html. However, the display is occupying the majority of the viewport to really showcase the image in display.
- This page is where the verified users will get to engage with one another via comments and likes.
- The like icon, unlike in index.html and blog.html, is an interactive button for verified users to like the post. Upon clicking this FontAwesome icon, the page with quickly refresh and display the icon in red.
- The comment secion is displayed for all users, however, the ability to add a comment is soley for verified users. In cases where the user is not verified, links will be provided to either log in at 'login.html' or to create an account with the site at 'signup.html'. If the user is verified they will be able to enter a comment in the provided text area and submit. At this time, the page will again, refresh and display the comment, now with an icon to delete. this icon will take the user to the 'edit_comment.html' template where they can confirm their choice. The user will not be able to edit the comment content so that the flow of conversation cannot be altered after the fact. This option is, of course, not available if the logged in user is not the author of the comment. 
- In cases where a verified user is viewing thier own post, the template will render two significant options below the comments secion. The first of which will be a button link to edit the post, upon submission, the user will be taken to the EditForm displayed on 'edit_post.html' template. Here the user is free to edit the title, caption, location, and status of the post. The slug is not an ediable field because it must always match the title. I have chosen not to allow users to change the image that defines thier post. This decision was made to ensure that no other users' comments would be underneath an imge that they did not see when writing said comment.
#### login.html
- The standard login form template from Django is styles to match the look of the rest of the site. It requests a username and a password, with the option to remember the login.
#### signup.html
- The standard signup form template from Django is styles to match the look of the rest of the site. It requests a username and a password that meets certain criteria.
#### logout.html 
- The standard logout form template from Django is styled to match the look of the site. It simply confirms that this action is desired.
#### Footer
- The footer element is identical across all pages of the site.
- It contains a list element containing anchors to various social media accounts (Instagram, Twitter) and to my GitHub.
- Each link is presented as a FontAwesome icon of each company.
#### Features to be added
- In the future I would like to add a drafts page for verified users, to view the unpublished saved posts that they have created.
- In the future I would like to add the ability for users with a certain amount of points, (as determined by the UserProfile model), to have some form of a 'super-like' functionality. Where they can like and star a post.
