<h1 align="center"> 

![Technical skills logo](static/image/logo.png) </h1>
Welcome to **Technical Skills!** This project is designed to help users access the most relevant courses for the technical skills they seek to learn. Whether you're a beginner looking to get started or an advanced user seeking specialized knowledge, Technical Skills has comprehensive suite of courses, and expert guidance to support your goals.

# Why Choose **Technical Skills?**

> - Simplifies the skill search process with a user-friendly interface.
> - Provides an intuitive course catalog and a robust search functionality.
> - Built with performance and scalability in mind, supporting thousands of users and courses.

View Live Site [Technical Skills](https://technical-skills-12c3cb7561cc.herokuapp.com/).

# ![am i responsive](readmeImages/responsive.png)

# Table of Contents
- [User Experience (UX)](#user-experience-ux)
  - [Project Management](#project-management)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Site Structure](#site-structure)
  - [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color Scheme](#color-scheme)
- [Data Model](#data-model)
- [Design Development](#design-development)
- [Features](#features)
  - [Header](#header)
  - [User Authentication and Authorization](#1-user-authentication-and-authorization)
  - [Course Management](#2-course-management)
  - [Course Category and Search](#3-course-category-and-search)
  - [Shopping Cart and Checkout](#4-shopping-cart-and-checkout)
  - [Order History and Enrollment](#5-order-history-and-enrollment)
  - [Admin Panel for Content and User Management](#6-admin-panel-for-content-and-user-management)
  - [Security and Privacy](#7-security-and-privacy)
  - [Registering a New Account](#registering-a-new-account)
  - [Logging In](#logging-in)
  - [Browsing Courses](#browsing-courses)
  - [Viewing Course Details](#viewing-course-details)
  - [Adding Courses to the Shopping Cart](#adding-courses-to-the-shopping-cart)
  - [Managing the Shopping Cart](#managing-the-shopping-cart)
  - [Checking Out and Making a Payment](#checking-out-and-making-a-payment)
  - [Viewing Order History](#viewing-order-history)
  - [Admin Features](#admin-features-for-admin-users-only)
  - [Navigation Bar](#navigation-bar)
  - [Footer](#footer)
  - [Error Page](#error-page)
  - [Social Links](#social-links)
- [Business Model](#business-model)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgment](#acknowledgment)

--- 
# User Experience (UX)

## Project Management
This project was managed using GitHub's project management tools to ensure organized and efficient development. GitHub Projects and Issues were utilized to create a Kanban-style workflow, which allowed the team to track progress and prioritize tasks effectively. Each task or bug was represented as an "Issue," and labeled based on its type (e.g., "feature," "bug," "enhancement") for quick categorization.

### The Kanban board
provided visibility into the project’s workflow by dividing tasks into stages, such as "To Do," "In Progress," and "Completed." This helped maintain an organized workflow, identify bottlenecks, and keep team members aligned on priorities.

Using GitHub’s tools allowed for seamless version control and communication within the team, ensuring that every change was documented and linked to the relevant tasks, fostering transparency and accountability across the project.

![Kanban board](readmeImages/Kanban.png)

[Back to top](#table-of-contents)

### Database Schema

This document outlines the database schema used in the e-learning Django project, describing each model and the relationships among them.
![database schema](readmeImages/model_diagram.png)

[Back to top](#table-of-contents)

## User Stories

### General User Stories
1. As a user, I want to create an account so that I can access my purchased courses and manage my profile.
2. As a user, I want to securely log in and log out of my account to protect my personal information.
3. As a user, I want the option to reset my password so that I can regain access if I forget it.
4. As a user, I want to browse available courses so that I can find one that interests me.
5. As a user, I want to filter courses by categories so that I can quickly find courses relevant to my interests.
6. As a user, I want to view a course's details so that I can understand its value before purchasing.
7. As a user, I want to add a course to my shopping cart so that I can continue browsing without losing my selection.
8. As a user, I want to proceed to checkout and pay securely so that I can purchase the course.
9. As a user, I want to access a list of all the courses I’ve purchased so that I can go back to them whenever I want.
10. As a user, I want my information to be stored securely so that I feel confident my data is protected.

### Admin User Stories
1. As an admin, I want to create, update, and delete courses so that I can manage the course offerings.
2. As an admin, I want to categorize courses so that users can easily find courses in specific areas of interest.
3. As an admin, I want to add and update images for each course so that users have a visual preview of what the course is about.
4. As an admin, I want to view a list of registered users so that I can monitor and manage user activities.
5. As an admin, I want to view a list of all orders so that I can track user purchases and sales data.
6. As an admin, I want to update the status of orders so that I can ensure all orders are correctly tracked.
7. As an admin, I want to view payment details and history for each order so that I can assist users with payment issues and verify transactions.

[Back to top](#table-of-contents)

---

## Wireframes
The wireframes for the site were created in the software Balsamiq. The wireframes have been created for desktop, tablet, and mobile devices. The text content wasn't finalized during the wireframe process. It's also worth mentioning that there are some visual differences in the deployed version compared to the original wireframes, the reason being design choices that were made during the creation process.

![Wireframes](readmeImages/homepage_wireframe.png)

[Back to top](#table-of-contents)

## Site Structure

The Technical Skills Website is a project focused on providing users with a structured, user-friendly platform for finding and accessing technical courses tailored to their skill levels. Built with modern web technologies such as Django, JavaScript, and Bootstrap, it is designed to support learners, professionals, and organizations by offering a comprehensive catalog of curated courses.

### **Key Features**

- **Course Discovery:** An intuitive interface for browsing, searching, and filtering courses by categories and user preferences.
- **Membership Access:** Registered members gain additional privileges like profile management, access to exclusive courses, and subscription management.
- **Customizable User Profiles:** Members can update their profile details, manage subscriptions, and tailor their learning paths.
- **Scalable and Responsive Design:** The website accommodates thousands of users and adjusts seamlessly to different devices, from desktops to mobile.
- **Admin Dashboard:** Tools for content management, user monitoring, and ensuring platform functionality.

### **Site Layout**

The site follows a hierarchical structure with clear navigation, making it easy for users to find courses, access resources, and interact with community features.

- **Non-Registered Users:** Can browse courses, view course details, and read user comments.
- **Registered Members:** Gain access to the member area and profile page upon successful registration, can pay for a course, and can rate and comment on brought courses.

### **Access for Members**

To gain access to the member area and profile page, users must complete the registration and payment process. This process begins on the 'Sign Up' page, accessible from the dropdown menu or the navigation bar when the site is viewed on smaller screens.

- **Payment System:** This is the sole point for accessing the payment system. If a user navigates away without completing the process, they must restart the procedure.
- **Post-Payment Access:** Once payment is successfully processed, a Member account receives the purchased course. Members can then access the Member Area and Profile Page.

### **Member Features**

Members can:

- View and update their profile.
- Modify their email address or password.
- Manage subscriptions (while this feature is not expected to be heavily used, it adds convenience).

The platform also supports future enhancements such as multilingual content, event registration, and gamification to improve engagement.

[Visit the live site here.](https://technical-skills-12c3cb7561cc.herokuapp.com/)

[Back to top](#table-of-contents)

---

## Design Choices

### Typography

- **Headings:** Montserrat, chosen for its professional and modern appeal.
- **Body Text:** Open Sans, selected for readability on all devices.

### Colour Scheme

- **Primary Color:** Blue - symbolizes trust and expertise.
- **Secondary Color:** White - ensures a clean and approachable design.
- **Accent Color:** Green - highlights actions and important elements.

![color palatte](readmeImages/palette-color.png)

[Back to top](#table-of-contents)

---

## Business Model

### Target Audience

- **Primary Users:** Individuals seeking technical skill development, including students, professionals, and hobbyists.
- **Secondary Users:** Employers and organizations interested in upskilling employees through curated courses.

### Value Proposition

- **For Learners:** A centralized platform offering tailored recommendations to guide users in finding courses aligned with their skill level, learning goals, and career aspirations.
- **For Organizations:** A resource for focused technical training and employee development.

### Revenue Streams

  1. **Course Sales:** Revenue from one-time purchases or subscriptions.
  2. **Featured Listings:** Paid promotions for course providers.
  3. **Corporate Partnerships:** Customized packages for organizations.
  4. **Affiliate Links:** Commissions earned through partnerships with external educational platforms.

### **Cost Structure**

- Platform development and maintenance.
- Marketing and outreach campaigns.
- Customer support services.

### **Key Partners**

- **Course Providers:** Subject matter experts and institutions.
- **Tech Platforms:** Payment processors and analytics tools.
- **Affiliate Partners:** External platforms offering complementary courses.

### **Channels**

- **Web Platform:** Main interface for course browsing and participation.
- **Email Marketing:** Personalized recommendations and updates.
- **Social Media:** Community engagement and course promotions.

---

## **Features**

Our platform is a simple and efficient e-learning marketplace built with Django, allowing users to explore, purchase, and enroll in courses. Below are the key features:

---

### Header

The header provides users with easy navigation and access to key features of the platform.

#### Features:
- **Logo:** A clickable logo that redirects to the homepage.
- **Dropdown Menus:** 
  - **Categories:** Allows users to browse courses by specific categories.
  - **Sort:** Enables users to sort courses based on criteria like price, popularity, or ratings.
- **Search Bar:** A quick way for users to search for courses by keywords.
- **Shopping Cart:** Displays items added to the cart and links to the checkout page.
- **Account Options:** 
  - **Login/Register:** Links for users to log in or register.
  - **User Profile:** Access to the user dashboard for logged-in users.

#### Preview:
![Header](readmeImages/header.png)

[Back to top](#table-of-contents)

### 1. User Authentication and Authorization
- **Secure Registration, Login, and Logout:** Robust user authentication for a secure experience.
- **Role-Based Permissions:** Separate access levels for regular users and admins.
- **Password Reset and Email Verification:** Users can reset forgotten passwords securely.
  
![Login](readmeImages/login.png)  
![Logout](readmeImages/logout.png)  
![Password Reset](readmeImages/profile.png)

[Back to top](#table-of-contents)

---

### 2. Course Management
- **Admin Dashboard:** Manage courses, including creating, updating, and deleting.
- **Categorization:** Organize courses into categories for easier discovery.
- **Detailed Course View:** Includes title, description, and cover image.  

![Course Management](readmeImages/admin-course-management.png)

[Back to top](#table-of-contents)

---

### 3. Course Category and Search
- **Organized Catalog View:** Browse courses by category and use filters for a tailored experience.
- **Search Functionality:** Quickly find courses using keywords.
  
![Categories](readmeImages/categories.png)  
![Search](readmeImages/search-categories.png)

[Back to top](#table-of-contents)

---

### 4. Shopping Cart and Checkout
- **Add/Remove Courses:** Easily manage selected courses in your shopping cart.
- **Secure Payment:** Integrated with Stripe for real-time payment processing.

![Cart Items](readmeImages/cart-addup.png)

[Back to top](#table-of-contents)

---

### 5. Order History and Enrollment
- **View Past Orders:** Access order history and download receipts.
- **Purchased Courses:** Easy access to all purchased content.

![Order History](readmeImages/orders.png)
![my learning profile](readmeImages/myLearningCourses.png)
![course to learn](readmeImages/MyCourse.png)

[Back to top](#table-of-contents)

---

### 6. Admin Panel for Content and User Management
- **Content Management:** Tools for managing courses, users, orders, and enrollments.
- **Sales and Analytics:** Monitor platform performance directly from the admin dashboard.

![Course Management](readmeImages/course-management.png)

[Back to top](#table-of-contents)

---

### 7. Security and Privacy
- **Environment Variable Management:** Protect sensitive data like SECRET_KEY and API keys.
- **Secure Payment Handling:** Uses Stripe for safe and reliable transactions.

![Password Reset](readmeImages/profile.png)

[Back to top](#table-of-contents)

---

## **Step-by-Step User Actions**

### Registering a New Account
1. Go to the **Register Page**.  
2. Fill in the required details (username, email, password).  
3. Submit the form and verify your email to activate your account.  

![Register Form](readmeImages/registerForm.png)

[Back to top](#table-of-contents)

---

### Logging In
1. Navigate to the **Login Page**.  
2. Enter your registered email and password.  
3. Upon successful login, you will be redirected to the homepage.  

![Login](readmeImages/login.png)

[Back to top](#table-of-contents)

---

### Browsing Courses
- Browse available courses from the homepage.  
- Filter courses by category or search for specific ones using keywords.  

![Search by Keywords](readmeImages/search-words.png)  
![All Courses](readmeImages/all-products.png)

[Back to top](#table-of-contents)

---

### Viewing Course Details
- Click on a course card to view details.  
- The tooltip provides a description, price, and an option to add the course to your cart.  

![Product Details](readmeImages/product-detail.png)

[Back to top](#table-of-contents)

---

### Adding Courses to the Shopping Cart
- From the course detail page, click **Add to Cart**.  
- Access your shopping cart anytime from the navigation bar.  

[Back to top](#table-of-contents)

---

### Managing the Shopping Cart
- Review and manage selected courses in your cart.  
- Remove unwanted courses or adjust quantities.  

![Add to Cart](readmeImages/item-added-to-cart.png)  
![Remove from Cart](readmeImages/delete-from-cart.png)

[Back to top](#table-of-contents)

---

### Checking Out and Making a Payment
1. Once your cart is ready, click **Checkout**.  
2. Enter payment details on the secure Stripe page.  
3. Complete the purchase and receive a confirmation page.  
4. **Note:** Use Stripe test card `4242 4242 4242 4242` for testing purposes.  

![Stripe Payment](readmeImages/paying-items.png)  
![Payment Confirmation](readmeImages/payed-item.png)

[Back to top](#table-of-contents)

---

### Viewing Order History
- Navigate to **My Account** and select **Order History** to view all purchased courses.

[Back to top](#table-of-contents)

---

### Admin Features (Admin Users Only)
- **Admin Dashboard:** Tools to create, edit, and delete courses.  
- **User Management:** Monitor user activity and manage permissions.  

![Create Course](readmeImages/create-course.png)
![Edit/Delete Course](readmeImages/edit-or-delete-course.png)

[Back to top](#table-of-contents)

### Social Links

The platform actively engages with the community through social media for updates, course promotions, and user interaction.

#### Features:
- **Facebook:** Stay updated with our latest course offerings and promotions.
- **Instagram:** Share and discover learning milestones and community stories.

#### Previews:
![Facebook](readmeImages/facebook-page.png)
![Instagram](readmeImages/instagram.png)

[Back to top](#table-of-contents)

---

### Error Page

A custom **404 Error Page** is displayed when users try to access a broken or non-existent link. This page helps guide users back to the site's main sections.

#### Features:
- **Friendly Message:** A clear explanation of the error.
- **Navigation Options:** Quick links to the homepage or other key sections.

#### Preview:
![Error 404](readmeImages/404.png)

[Back to top](#table-of-contents)

---

### Footer

The footer provides essential information and links, creating a consistent and polished user experience across all pages.

#### Features:
- **Copyright Notice:** Ensures legal compliance and branding.
- **Newsletter Subscription:** Allows users to stay updated on new courses and promotions.
- **Social Media Links:** Quick access to the platform’s social media accounts.

#### Preview:
![Footer](readmeImages/footer.png)

[Back to top](#table-of-contents)

---


# Business Model
# ![main](readmeImages/main.png)
1. ## Target Audience
	- **Primary Users**: Individuals seeking to learn or reinforce technical skills but unsure of where to begin or which courses to take.
	- **Secondary Users**: Employers or organizations looking to upskill employees through curated courses.
2. ## Value Proposition
	- **For Learners**: A centralized platform offering tailored recommendations to guide users in discovering courses that align with their skill level, learning goals, and career ambitions.
	- **For Organizations**: A resource for enabling focused technical training and skill development for employees.
3. ## Revenue Streams
	- **Course Sales**: Revenue generated from one-time course purchases or subscriptions.
	- **Featured Course Listings**: Paid placement for course providers to have their courses featured prominently on the platform.
	- **Corporate Partnerships**: Offering tailored packages for companies interested in upskilling employees, potentially with bulk pricing or access to exclusive content.
	- **Affiliate Links**: Earning a commission by partnering with other educational platforms or providers and directing traffic through affiliate links.
4. ## Cost Structure
	- **Platform Development & Maintenance**: Regular updates, bug fixes, and feature improvements to ensure a seamless user experience.
	- **Marketing & Outreach**: Campaigns targeting learners and organizations through social media, SEO, content marketing, and partnerships.
	- **Customer Support**: Providing support for learners and partners to improve satisfaction and resolve issues.
5. ## Key Partners
	- **Course Providers**: Partnering with subject matter experts, institutions, and tech platforms to offer diverse, high-quality courses.
	- **Tech Platforms**: Integrations with payment processors (like Stripe) and analytics tools to enhance service offerings.
	- **Affiliate Partners**: External platforms that offer specialized or complementary courses to expand course options.
6. ## Channels
	- **Web Platform**: The main interface for users to browse, purchase, and participate in courses.
	- **Email Marketing**: Reaching out to users with new course recommendations, discounts, and personalized learning suggestions.
	- **Social Media Presence**: Engaging with the community, sharing success stories, and promoting trending courses.
8. ## Key Activities
	- **Platform Development**: Regularly developing new features, ensuring compatibility, and maintaining high usability.
	- **Course Curation & Quality Control**: Selecting and featuring courses that align with user needs and maintain high standards.
	- **Marketing & Customer Acquisition**: Implementing strategies to attract new users and improve brand visibility.

# Marketing Techniques
1. ## Social Media Campaigns
	- **Targeted Ads**: Use ads on platforms like Facebook, Instagram, and LinkedIn, focusing on audiences interested in skill-building and professional development.
	- **Influencer Partnerships**: Collaborate with industry influencers or tech educators who can share insights about the courses available on the platform.
	- **Live Sessions & Webinars**: Host free live sessions, webinars, or Q&As on social channels to demonstrate the value of selected courses.

2. ## Email Marketing
	- **Personalized Course Recommendations**: Send emails with course suggestions based on users' interests, previous searches, or completed courses.
	- **Weekly Newsletters**: Share the latest courses, learning resources, and trending tech topics in a newsletter format.
	- **Promotional Campaigns**: Offer discounts on popular courses during peak enrollment times, such as the start of the year, new job cycles, or key industry events.

3. ## Search Engine Optimization (SEO)
	- **Keyword Targeting**: Optimize the website and course descriptions for terms such as “learn tech skills,” “beginner coding courses,” and “best online tech courses.”
	- **Technical SEO**: Improve load times, mobile responsiveness, and accessibility to rank higher in search results.
	- **Backlinking**: Build partnerships and gain backlinks from reputable tech blogs, educational websites, and industry publications to boost site authority.

4. ## Affiliate & Referral Program
	- **Referral Incentives**: Reward users who refer friends with discounts on their next course or access to exclusive content.
	- **Affiliate Partnerships**: Collaborate with career development websites, tech bloggers, and educational platforms to promote courses and receive commissions on sales generated through affiliates.

5. ## Corporate Partnerships and B2B Outreach
	- **Upskilling Programs for Businesses**: Market directly to businesses interested in upskilling employees, offering volume discounts and custom learning paths.
	- **LinkedIn Outreach**: Network with HR and L&D professionals on LinkedIn, promoting the platform as a valuable resource for employee development.

6. ## Community Building
	- **Discussion Forums & Peer Support**: Create a space where users can ask questions, share learning experiences, and get advice, fostering a community feeling.
	- **User-Generated Content**: Encourage users to share their projects, code snippets, or experiences, and feature the best examples on the platform’s social channels or blog.

7. ## Influencer & Industry Partnerships
	- **Guest Appearances on Podcasts and Webinars**: Partner with influencers or thought leaders to appear in their content, introducing the platform to a wider audience.
	- **Collaborations with Online Tech Communities**: Work with platforms like GitHub, Stack Overflow, or specialized subreddits to engage with users in their preferred learning spaces.

8. ## Paid Advertising
	- **Google Ads & Retargeting**: Use Google Ads to reach users searching for technical courses and retarget site visitors who didn’t complete purchases.
	- **Seasonal & Limited-Time Offers**: Run promotional campaigns around significant times like "Back to School" or "New Year, New Skill" campaigns to capitalize on users’ learning motivations.

[Back to top](#table-of-contents)

---

## Technologies Used
### Main Language
- Python Language

### Frameworks, Libraries & Programs

- [**AmIResponsive**](https://ui.dev/amiresponsive) - the responsive preview image on different gadgets.
- [**iloveimg**](https://www.iloveimg.com/) - to compress the images.
- [**Google Fonts**](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.
- [**Schemas**](https://app.diagrams.net/) - to create database structure.

- [**Django/Jinja**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)
- [**Gitpod**](https://gitpod.com/) - online IDE - gitpod was used to create this project
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control
- [**Heroku**](https://heroku.com) - to deploy this project
- [**Google Fonts**](https://fonts.google.com/) - used for picking the best typography
- [**PostgresSQL**](https://www.postgressql.com/) - used as a database storage
- [**Cloudinary**](https://console.cloudinary.com/) - used as a storage of static files
- [**FavIcon.io**](https://favicon.io/favicon-converter/) - used to compress favicon
- [**W3Schools**](https://www.w3schools.com/) - useful information and cheat sheets
- [**Google Fonts**](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

[Back to top](<#table-of-contents>)

# Testing
## User Stories testing
Below the user stories for the project are listed to clarify why particular feature matters. These will then be tested and confirmed in the Testing section.

## 1. User Registration and Authentication
  - As a user, I want to be able to create an account so that I can access my purchased courses and manage my profile.
  - As a user, I want to securely log in and log out of my account to protect my personal information.
  - As a user, I want the option to reset my password so that I can regain access if I forget it.
## 2. Course Browsing and Discovery
  - As a user, I want to browse available courses so that I can find one that interests me.
  - As a user, I want to filter courses by categories (e.g., Development, Design, Marketing) so that I can quickly find courses relevant to my interests.
  - As a user, I want to view a course's details, such as the description, category, price, and an image, so that I can understand its value before purchasing.
## 3. Shopping Cart and Checkout
  - As a user, I want to add a course to my shopping cart so that I can continue browsing without losing my selection.
  - As a user, I want to view the contents of my cart so that I can review my selections before purchasing.
  - As a user, I want to remove courses from my cart if I change my mind before checkout.
  - As a user, I want to proceed to checkout and pay using Stripe so that I can securely purchase the course.
## 4. Payment Processing with Stripe
  - As a user, I want a secure and reliable payment process so that I can confidently complete my purchase.
  - As a user, I want to receive an email confirmation and a receipt after I’ve made a payment so that I have a record of my purchase.
## 5. Accessing Purchased Courses
  - As a user, I want to access a list of all the courses I’ve purchased so that I can go back to them whenever I want.
  - As a user, I want to be able to download any resources associated with the course so that I can review them offline if needed.
## 6. Course Management (Admin)
  - As an admin, I want to be able to create, update, and delete courses so that I can manage the course offerings.
  - As an admin, I want to categorize courses by topic or difficulty so that users can filter courses easily.
  - As an admin, I want to view sales and order histories so that I can understand the platform’s performance and popular courses.
## 7. User Profile Management
  - As a user, I want to update my personal information (like name, email) in my profile so that it stays accurate and up-to-date.
  - As a user, I want to view my order history and purchase details so that I can keep track of my learning investments.
## 8. Security and Privacy
  - As a user, I want my information to be stored securely and to feel confident my data is protected.
  - As a user, I want to receive notifications of any important updates or security-related changes so that I can stay informed and secure.
## 9. UI and User Experience
  - As a user, I want a clean, intuitive interface so that I can easily navigate and find the courses I need.
  - As a user, I want a responsive design so that I can access the platform easily from my phone, tablet, or desktop.
## 10. Notifications and Receipts
  - As a user, I want to receive a notification upon completing a purchase so that I’m immediately aware of my successful order.
  - As a user, I want an emailed receipt and access to my invoice details so that I have a permanent record of my transaction.

[Back to top](<#table-of-contents>)

## Admin User Stories Testing
## 1. Course Management
  - As an admin, I want to create, update, and delete courses, so that I can keep the course offerings current and relevant for users.
  - As an admin, I want to categorize courses, so that users can easily find courses in specific areas of interest.
  - As an admin, I want to add and update images for each course, so that users have a visual preview of what the course is about.
## 2. User Management
  - As an admin, I want to view a list of registered users, so that I can monitor and manage user activities.
  - As an admin, I want to activate or deactivate user accounts, so that I can control access for users who violate terms or security policies.
  - As an admin, I want to assign different roles users, so that responsibilities are clear within the admin team.
## 3. Order and Payment Management
  - As an admin, I want to view a list of all orders, so that I can track user purchases and sales data.
  - As an admin, I want to update the status of orders (e.g., processing, completed), so that I can ensure all orders are correctly tracked.
  - As an admin, I want to view payment details and history for each order, so that I can assist users with payment issues and verify transactions.

[Back to top](<#table-of-contents>)

## Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design](https://ui.dev/amiresponsive).
Tested across devices and browsers for seamless functionality and appearance.  
- **Devices:** Desktop, tablet, and various mobile devices  


| Desktop    | Display > 1280px      | Display < 1280px   |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Links      | pass                  | pass               |
| Images     | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |

| Phone      |Galaxy S5/S6/S7/S20+   | iPhone 6/7/8/ plus | iPhone 14pro max     |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-contents>)

## Browser Compatibility Testing
`Technical skills` blog was tested for functionality and appearance in the following browsers on desktop. No visible or funcional issues on all 
the browsers below.
- **Browsers:** Chrome, Firefox, Edge

[Back to top](<#table-of-content>)

# Testing

- Lighthouse testing: ![Performance diagnodtics](readmeImages/lighthouse.png)
  
## Validator Testing

- [HTML Checker](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechnical-skills-12c3cb7561cc.herokuapp.com%2F)

  ![HTML checker](readmeImages/html-validator.png)
  - There are no errors but 4 footer h1 warnings found but if changed it could look smaller.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

  ![CSS results](readmeImages/css-Validator.png)
  - There are no errors but 30 warnings found due to django framework.

-
- [Web Accessibility Evaluation Tool Validator](https://wave.webaim.org/report#/https://technical-skills-12c3cb7561cc.herokuapp.com/)
  ![WebAim](readmeImages/wave.png)
   - There are no errors or alerts bur 3 contrast errors found due to boostrap.


# Deployment

Follow these steps to deploy the Technical Skills course platform on **Heroku**. This guide covers setting up static files, environment variables, and Stripe integration for payment processing.

---

### Prerequisites
- **Heroku Account**: Sign up at [Heroku](https://www.heroku.com/).
- **Heroku CLI**: Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for managing deployments.
- **Git**: Required for pushing code to Heroku.

---

### Preparing the Django Project

1. **Install Gunicorn and Whitenoise**:
   - Install Gunicorn (WSGI server for production) and Whitenoise (for static file handling):
     ```bash
     pip install gunicorn whitenoise
     ```

2. **Update `requirements.txt`**:
   - Freeze dependencies for Heroku:
     ```bash
     pip freeze > requirements.txt
     ```

3. **Create a `Procfile`**:
   - In the project root, create a `Procfile` (no extension) to specify how Heroku should run the project:
     ```plaintext
     web: gunicorn <project_name>.wsgi
     ```
     Replace `<project_name>` with your Django project folder name (contains `settings.py`).

4. **Configure Static Files**:
   - Update static file settings in `settings.py`:
     ```python
     STATIC_ROOT = BASE_DIR / "staticfiles"
     STATIC_URL = "/static/"

     # Add Whitenoise Middleware
     MIDDLEWARE = [
         "whitenoise.middleware.WhiteNoiseMiddleware",
         # other middlewares
     ]
     STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
     ```

5. **Database Configuration**:
   - Install `dj-database-url` to handle Heroku’s PostgreSQL:
     ```bash
     pip install dj-database-url
     ```
   - Update `DATABASES` in `settings.py` to use Heroku’s database:
     ```python
     import dj_database_url
     DATABASES = {
         "default": dj_database_url.config(default="sqlite:///db.sqlite3")
     }
     ```

6. **Environment Variables**:
   - Use environment variables for sensitive data like `SECRET_KEY`, `DEBUG`, and Stripe API keys:
     ```python
     import os
     SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
     DEBUG = os.getenv("DEBUG", "False") == "True"
     STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
     STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
     ```

[Back to top](<#table-of-contents>)
---

### Deploying to Heroku

1. **Log In to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a New Heroku App**:
  ```bash
    heroku create your-app-name
    Replace your-app-name with a preferred name, or omit it for a random name.
  ```

3. **Set Up Environment Variables**:
  - Configure environment variables on Heroku:
    ```bash
      heroku config:set SECRET_KEY='your-secret-key'
      heroku config:set DEBUG=False
      heroku config:set STRIPE_PUBLIC_KEY='your-stripe-public-key'
      heroku config:set STRIPE_SECRET_KEY='your-stripe-secret-key'
      Add Heroku PostgreSQL:
    ```

4. **Add a PostgreSQL database to your Heroku app**:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    Push Code to Heroku:
    ```

5. **Initialize Git, add, and commit the code if not already done**:
    ```bash
    Copy code
    git init
    git add .
    git commit -m "Initial commit"
    ```
6. **Push code to Heroku**:
    ```bash
    git push heroku main
    ```
7. **Run Migrations**:
  - Apply migrations on Heroku:
  ```bash
  heroku run python manage.py migrate
  ```
8. **Create a Superuser**:

  - Set up a superuser to access the admin interface:
  ```bash
  heroku run python manage.py createsuperuser
  Testing the Deployment
  ```
9. **Access the Application**:
  - Open your app in a browser:
  ```bash
  heroku open
  ```
10. **Test Stripe Payments (Sandbox)**:
  - Use Stripe test card 4242 4242 4242 4242 to test transactions.
11. **Monitor Logs**:
  - Check logs for any issues:
  ```bash
  heroku logs --tail
  ```
[Back to top](<#table-of-contents>)

## **Credits**

### **Content**

Written and curated by the Technical Skills developer.

---

### **Media**

- [Pexels](https://www.pexels.com/): Images sourced under proper permissions.
- [iloveimg](https://www.iloveimg.com/): Used for image compression.
- [Kaggle](https://www.kaggle.com/datasets/yusufdelikkaya/udemy-online-education-courses): Provided JSON file data for course information.
- [csvjson](https://csvjson.com/csv2json): Tool for converting CSV files to JSON format.

---

### **Frameworks and Tools**

- **HTML5**: Core structure and semantics of the website.
- **Bootstrap 5**: Used for responsive design, grid layout, navigation bar, modals, and other components.
  - [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/)
  - Customizations applied for color schemes, typography, and UI elements.
- **Django Framework**: Backend logic, database management, and API integration.
  - [Django Documentation](https://www.djangoproject.com/)
  - [Django Admin Site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/) for superuser interface setup.
  - [Django Model `__str__`](https://docs.djangoproject.com/en/5.0/ref/models/instances/) for managing model string representations.
  - [Django Templates](https://docs.djangoproject.com/en/5.0/topics/templates/) for template rendering.
  - [Django Time Zone Support](https://docs.djangoproject.com/en/5.0/topics/i18n/) for internationalization settings.
  - [Django Password Validation](https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators) for authentication security.
- **JavaScript & jQuery**:
  - [jQuery Post API](https://api.jquery.com/jQuery.post/) for handling AJAX requests.
  - Dynamic form submission using [Ajax Form Submission Guide](https://youtu.be/KgnPSmrQrXI?si=Y1Whk2AATEYZB1Dz).
- **FontAwesome**: Icons for navigation and interactive components.
  - [FontAwesome Documentation](https://fontawesome.com/)
- **CSS3**: Custom styles to enhance the Bootstrap 5 components.
- **Color Contrast Checker**: Ensured color scheme accessibility using [Coolors](https://coolors.co/contrast-checker/112a46-acc8e5).
- **Color Palette**: [Coolors](https://coolors.co/ffc107-0dcaf0-ffffff-dc3545-198754)

[Back to top](<#table-of-contents>)
---

### **Acknowledgements**

The application **Technical Skills** was developed as Portfolio Project 5 for the Full Stack Software Development Diploma at the [Code Institute](https://codeinstitute.net/).

#### Special Thanks:

- **Mentor**: Precious Ijege for providing valuable feedback and guidance throughout the project.
- [Dave Gray's YouTube Channel](https://youtu.be/Rp5vd34d-z4?si=Iau1px_g565k1H3y) for tutorial support and additional insights.
- [Code Institute](https://codeinstitute.net/) for offering comprehensive resources for software development.
- [Stack Overflow](https://stackoverflow.com/) for solutions to coding challenges and community support.

---

### **Documentation and Tutorials**

- [GeeksforGeeks Jinja Tutorial](https://www.geeksforgeeks.org/jinja-for-server-side-rendering-in-django/) for Jinja templating techniques.
- [Bootstrap 5 Components](https://getbootstrap.com/docs/5.0/components/) for creating a responsive design.
- [User Authentication Guide](https://youtu.be/WuyKxdLcw3w?si=a_-3HyADtu5sblOR) for secure user management.

---

### **Testing and Development Tools**

- **Browser Compatibility Testing**: Verified performance on Chrome, Firefox, and Edge.
- **Responsiveness Testing**: Ensured seamless performance on desktops, tablets, and mobile devices.
- **Version Control**: Managed using Git and GitHub for consistent code updates and collaboration.

---

## Developed
  - *[Elsie Nagawa ](https://github.com/EIN-1/justask)
  - 29.12.2024

  [Back to top](<#table-of-contents>) 
