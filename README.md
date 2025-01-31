# MusicMatch App

## Table of Contents

# MusicMatch App

## Table of Contents

1. [Introduction](#introduction)
2. [Overview](#overview)
3. [UX - User Experience](#ux---user-experience)
   - [Design Inspiration](#design-inspiration)
   - [Colour Scheme](#colour-scheme)
   - [Fonts](#fonts)
4. [Project Planning](#project-planning)
   - [Strategy Plane](#strategy-plane)
   - [Site Goals](#site-goals)
   - [Agile Methodologies](#agile-methodologies)
   - [MoSCoW Prioritization](#moscow-prioritization)
   - [Sprints](#sprints)
5. [User Stories](#user-stories)
   - [Must-Have Features ✅](#must-have-features-✅)
   - [Should-Have Features ⏳](#should-have-features-⏳)
   - [Could-Have Features 🚀](#could-have-features-🚀)
6. [Scope Plane, Structural Plane, Skeleton and Surface Planes](#scope-plane-structural-plane-skeleton-and-surface-planes)
   - [Scope Plane](#scope-plane)
   - [Structural Plane](#structural-plane)
   - [Skeleton Plane](#skeleton-plane)
   - [Surface Plane](#surface-plane)
7. [Attendee Features](#attendee-features)
8. [Event Holder Features](#event-holder-features)
9. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
   - [ERD Image](#erd-image)
   - [Overview](#overview-1)
   - [How It Works](#how-it-works)
   - [Security](#security)
     - [CSRF Tokens](#csrf-tokens)
     - [Role-Based Access Control](#role-based-access-control)
     - [Defensive Design](#defensive-design)
     - [Data Management](#data-management)
10. [User View - Registered/Unregistered](#user-view---registeredunregistered)
11. [CRUD Functionality](#crud-functionality)
12. [Feature Showcase](#feature-showcase)
    - [Header/Navigation & Footer](#headernavigation--footer)
    - [Home Page](#home-page)
    - [Registration/Sign-Up](#registration-or-sign-up)
    - [Profile](#profile)
    - [Events](#events)
    - [Bookings](#bookings)
13. [Admin Panel](#admin-panel)
14. [Future Development](#future-development)
15. [Technologies & Tools Used](#technologies--tools-used)
16. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloning the Repository](#cloning-the-repository)
    - [Forking the Repository](#forking-the-repository)
17. [AI Tools in Development](#ai-tools-in-development)
    - [Using AI to Assist in Code Creation](#using-ai-to-assist-in-code-creation)
    - [Using AI to Assist in Debugging](#using-ai-to-assist-in-debugging)
    - [Using AI to Optimize Code for Performance and UX](#using-ai-to-optimize-code-for-performance-and-ux)
    - [Using AI to Create Automated Unit Tests](#using-ai-to-create-automated-unit-tests)
    - [Reflection on AI’s Role in the Development Process](#reflection-on-ais-role-in-the-development-process)
18. [Testing](#testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Testing User Stories](#testing-user-stories)
    - [Device Testing](#device-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Accessibility](#accessibility)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
19. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
    - [Additional Reading/Tutorials](#additional-reading-and-tutorials)

---

## Introduction

**MusicMatch** is a dynamic music event booking platform designed for the vibrant music scene in the UK. Built as a beginner Django project, MusicMatch focuses on enabling hosts to showcase their events while allowing users to easily book tickets. It leverages responsive design, CRUD functionality, and database management to deliver an intuitive and functional user experience.

MusicMatch was developed for educational purposes as part of my journey to learn Django and further my skills in full-stack web development using Python, Bootstrap frameworks, and AI tools such as Microsoft Co-Pilot and DALL-E.

**View the live site here:** [MusicMatch Live Site](https://music-match-483fb192c3d8.herokuapp.com/)  
**Admin access with relevant sign-in information:** [MusicMatch Admin Login](https://music-match-483fb192c3d8.herokuapp.com/admin)

---

## Overview

MusicMatch is a responsive, user-friendly booking platform catering to music enthusiasts and event organisers. The website allows users to:

- View a list of upcoming music events.
- Register and log in to book tickets for events.
- Enable hosts to create, publish, and manage events.
- Deliver a seamless mobile-first experience for easy navigation and booking.

MusicMatch seeks to address the needs of Sheffield’s vibrant music community by providing a centralised platform to connect event hosts and attendees. This MVP (Minimum Viable Product) is the foundation for further enhancements such as payment integration and advanced search features.

---

## UX - User Experience

### Design Inspiration

The design was inspired by the thriving music culture of the UK and the need for a modern, clean interface for users to interact with the platform easily. The focus was on simplicity and functionality, ensuring users could find and book events with minimal effort. Using calming fonts (Poppins for headlines and Lato for body text) enhances readability and maintains a professional, welcoming aesthetic.

### Colour Scheme

The colour palette was selected to reflect the UK’s vibrant yet grounded music scene, inspired by the 1970s with a modern-day minimalist design approach.  
Key colours include:

- **Primary:** Calm green for navigation and background (`#c9dbba`)
- **Secondary:** Bright orange accents for calls to action (`#faa381`)
- **Tertiary:** Light green and white for clarity and contrast (`#75704e`)

![alt text](media/image.png)

### Fonts

The website uses the following fonts, both imported from Google Fonts:

- **Poppins:** A clean and modern sans-serif font for headlines.
- **Lato:** A versatile sans-serif font for body text, ensuring optimal readability.

---

## Project Planning

### Strategy Plane

The core goal was to create a booking platform that bridges the gap between event hosts and attendees. The MVP ensures users can browse events, register/log in, and book tickets, while hosts can create and manage their events.

#### Site Goals

- Build a responsive website for easy access on all devices.
- Deliver an intuitive UI for a smooth user experience.
- Create scalable features to support future enhancements such as payment processing.

### Agile Methodologies

Using **GitHub Projects**, tasks were organized into user stories, development tasks, and testing tasks. Agile methodologies ensured timely delivery of the MVP, with room for additional features based on available time.

### MoSCoW Prioritization

- **Must-Have:** User registration, event listing, ticket booking, mobile responsiveness.
- **Should-Have:** Search and filter functionality, basic host dashboard, booking confirmation page.
- **Could-Have:** Simulated email confirmation, simple event search by date.
- **Won’t-Have:** Payment processing and advanced analytics in this phase.

### Sprints

Sprint planning ensured steady progress:
| Sprint | Content | Start Date | End Date |
|--------|---------------------------------|---------------|---------------|
| #1 | Project Setup & Database Design | Jan 10, 2025 | Jan 12, 2025 |
| #2 | User Authentication & Navigation | Jan 12, 2025 | Jan 15, 2025 |
| #3 | Event Creation & Booking | Jan 15, 2025 | Jan 19, 2025 |
| #4 | Frontend Design | Jan 20, 2025 | Jan 23, 2025 |
| #5 | Testing & Deployment | Jan 23, 2025 | Jan 25, 2025 |

---

## User Stories

### Must-Have Features ✅

1. **View List of Upcoming Events**

   - **User Story:** As a site user, I can view a list of upcoming music events in Sheffield, so that I can decide which event to attend.
   - **Acceptance Criteria:**
     - Given multiple events exist in the database, then they are displayed on the homepage.
     - When a user visits the homepage, then they see event titles, dates, and venues.

2. **User Registration and Login**

   - **User Story:** As a site user, I can register and log in to the site, so that I can book tickets for events.
   - **Acceptance Criteria:**
     - Given a registration form, then users can create an account with a username, email, and password.
     - When a user logs in, then they can access event booking features.

3. **Host Event Creation**

   - **User Story:** As an event host, I can create and publish new music events, so that users can discover and book my events.
   - **Acceptance Criteria:**
     - Given that a host is logged in, then they can access an event creation form.
     - When the host submits event details (title, description, date, venue), then the event is displayed on the homepage.

4. **Book a Ticket for an Event (Without Payment Integration)**

   - **User Story:** As a site user, I can book a ticket for an event, so that I can attend it.
   - **Acceptance Criteria:**
     - Given that the user is logged in, then they can click a “Book Now” button on event pages.
     - When the user confirms the booking, then a success message is displayed and the booking is saved.

5. **Mobile-Responsive Design**
   - **User Story:** As a site user, I can access the website on my mobile device, so that I can browse and book events easily.
   - **Acceptance Criteria:**
     - Given the user is on a mobile device, then the website layout adjusts to fit the screen.
     - When browsing events, then the interface remains easy to navigate.

### Should-Have Features ⏳

6. **Search and Filter Events**
7. **Basic Host Dashboard (View Events Only)**
8. **Booking Confirmation Page**

### Could-Have Features 🚀

9. **Simulated Email Confirmation**
10. **Simple Event Search by Date**

---

## Scope Plane, Structural Plane, Skeleton and Surface Planes

| Feature               | Visitors | Registered Users |
| --------------------- | -------- | ---------------- |
| View Events           | Yes      | Yes              |
| Book Tickets          | No       | Yes              |
| Host Dashboard        | No       | Yes (Hosts Only) |
| Mobile Responsiveness | Yes      | Yes              |
| CRUD Functionality    | No       | Yes              |

### Scope Plane

The scope of **MusicMatch** focuses on addressing key needs for both event organizers and attendees. The primary aim is to create a user-friendly platform where:

- Users can explore, register, and book tickets for events with ease.
- Event hosts can create, manage, and promote events effectively.

#### Essential Features:

- User registration and authentication.
- Event creation by hosts.
- Event browsing and ticket booking.
- Responsive design for all devices.

## Attendee Features

<details>
<summary>View Attendee Features</summary>

![alt text](media/image-1.png)  
![alt text](media/image-2.png)  
![alt text](media/image-3.png)  
![alt text](media/image-4.png)

</details>

---

## Event Holder Features

<details>
<summary>View Event Holder Features</summary>

![alt text](<media/Screenshot 2025-01-26 at 22.14.56.png>)  
![alt text](<media/Screenshot 2025-01-26 at 22.20.00.png>)  
![alt text](<media/Screenshot 2025-01-26 at 22.17.55.png>)  
![alt text](<media/Screenshot 2025-01-26 at 22.18.51.png>)

</details>

#### Future Scope:

- Integration of payment gateways.
- Advanced search options, including artist and genre-based filters.
- Email notifications and reminders for bookings.
- Enhanced host dashboards with analytics and ticket management.

---

### Structural Plane

The structural design of **MusicMatch** ensures logical organization and easy navigation. Core elements were developed to cater to both functional requirements and user interaction flow.

#### Navigation Design:

- A clear, top navigation bar provides direct access to key sections: Home, Events, Login, and Host Dashboard.
- Conditional links based on user roles (attendees vs. hosts).

#### Page Layout:

- **Events Listing Page:** Features a card-based design, with event titles, dates, and venues clearly displayed.
- **Host Dashboard:** Displays a list of hosted events with options to edit or delete events.
- **Mobile Responsiveness:** Bootstrap grid classes and custom CSS ensure seamless transitions between devices.

#### Accessibility:

- Added ARIA roles and semantic HTML tags for screen readers.
- Tooltips for icons and form fields provide extra guidance for users.

---

### Skeleton Plane

The skeleton phase involved creating wireframes to map out user interactions and content placements. These were designed to prioritize intuitive navigation and visually balanced layouts.

#### Wireframe Highlights:

Mobile/Tablet/Desktop Homepage:
![alt text](media/Homepage_Wireframe.png)

Register:
![alt text](media/Register.png)

Login:
![alt text](media/Login.png)

Customer Upcoming Events:
![alt text](media/Upcoming_Events.png)

Customer Booked Events:
![alt text](media/Booked_Events.png)

Event Holder Made Events:
![alt text](media/My_Events.png)

Event Holder Create Events:
![alt text](media/Create_Event.png)

- **Homepage:**
  - Hero section with a welcome message and CTA buttons for exploring events or signing up.
  - Upcoming events preview with a "View All Events" link.
- **Event Details Page:**
  - Displays detailed information about the event, including date, time, and venue.
  - A prominent "Book Now" button for ticket reservation.
- **Host Dashboard:**
  - A list of events created by the host, with action buttons for editing or deleting events.

#### Design Tools Used:

- Wireframes were created using Balsamiq to ensure precision and clarity.
- Focus on a grid-based layout to ensure modularity.

---

### Surface Plane

The surface plane of **MusicMatch** focuses on the aesthetics and visual appeal while maintaining usability.

#### Colour Scheme:

- **Primary:** `#faa381` (light orange) for action buttons and highlights.
- **Secondary:** `#c9dbba` (muted green) for backgrounds and soft accents.
- **Accent:** `#75704e` (dark olive) for text and subtle elements.

#### Typography:

- **Poppins:** Used for headings to create a modern and approachable look.
- **Lato:** Used for body text to ensure readability and clean presentation.

#### UI Enhancements:

- Buttons with hover animations to provide feedback on interactions.
- Rounded corners and shadows on cards for a polished appearance.
- Icons sourced from FontAwesome for intuitive and consistent visual cues.

#### Responsive Design:

- Media queries ensure that elements scale and adjust seamlessly across devices.
- Forms and tables are optimized for smaller screens without sacrificing functionality.

---

Conclusion

The integration of the **Scope**, **Structural**, **Skeleton**, and **Surface** planes ensures that **MusicMatch** delivers a cohesive and delightful experience for all users. These foundational design principles provide a scalable framework to enhance the platform in future iterations.

## **Database Schema - Entity Relationship Diagram**

The following describes the structure of the database and the relationships between entities:

### Entities

#### 1. **User**

- This is provided by Django's built-in User model.
- **Fields**:
  - `id`
  - `username`
  - `email`
  - `password`
  - (Other default fields from the Django User model)

#### 2. **Profile**

- **Fields**:
  - `id`
  - `user_id` (One-to-One relationship with `User`)
  - `role` (e.g., Customer or Event Holder)
  - `venue_name` (optional, applicable to Event Holders)
- **Relationship**: One-to-One with `User`

#### 3. **Event**

- **Fields**:
  - `id`
  - `title` (Event title)
  - `bio` (Event description)
  - `venue` (Venue name)
  - `street` (Street address)
  - `city` (City of the event)
  - `postcode` (Postcode of the event)
  - `date` (Event date and time)
  - `music_genre` (Event genre, e.g., Rock, Pop, etc.)
  - `organizer_id` (ForeignKey to `User`, representing the event organizer)
- **Relationship**: Many-to-One with `User` (as organizer)

#### 4. **Booking**

- **Fields**:
  - `id`
  - `user_id` (ForeignKey to `User`)
  - `event_id` (ForeignKey to `Event`)
  - `booked_on` (Timestamp of booking)
  - `ticket_count` (Number of tickets booked)
- **Relationships**:
  - Many-to-One with `User` (as the booking user)
  - Many-to-One with `Event` (as the booked event)

---

### Relationships

1. **User and Profile**:

   - A `User` can have **one Profile** (One-to-One relationship).
   - A `Profile` is associated with exactly one `User`.

2. **User and Events**:

   - A `User` can organize **multiple Events** (One-to-Many relationship).
   - An `Event` is associated with one `User` (as the organizer).

3. **User and Bookings**:

   - A `User` can make **multiple Bookings** for different events (One-to-Many relationship).
   - A `Booking` is associated with one `User`.

4. **Event and Bookings**:
   - An `Event` can have **multiple Bookings** associated with it (One-to-Many relationship).
   - A `Booking` is associated with one `Event`.

### **ERD Image**

![alt text](media/ERD.png)

---

### **Overview**

The **Entity Relationship Diagram (ERD)** for MusicMatch demonstrates the relationships between the various components of the application and how they connect to the underlying PostgreSQL database. It outlines how users, events, bookings, and profiles are interlinked.

MusicMatch leverages Django’s built-in `User` model for user authentication and authorization. When a user registers, a `user_id` is created, which acts as a unique identifier linking them to other key features such as creating and managing events, making bookings, and editing their profile. This ensures seamless data connectivity across the platform.

---

### **How It Works**

1. **User Authentication**:

   - Django's `User` model handles registration and login functionalities.
   - A `Profile` model is linked to the `User` model using a one-to-one relationship. This allows for role-based differentiation (e.g., `customer` or `event_holder`).

2. **Events and Bookings**:

   - Users with the `event_holder` role can create and manage `Event` entries.
   - Users (both `customers` and `event_holders`) can book tickets for events. The `Booking` model links users to specific events, with attributes like ticket count and booking time.

3. **Django Admin Panel**:
   - Administrators can view and manage all data, including events, profiles, and bookings, through Django’s Admin dashboard.
   - Data integrity is ensured with `on_delete=models.CASCADE`, meaning when a user is deleted, all their related data (e.g., events, bookings) is automatically removed.

---

### **Security**

A range of measures were implemented to protect user data and ensure the platform operates securely:

#### **1. CSRF Tokens**

- Every form submission includes CSRF (Cross-Site Request Forgery) tokens to validate requests and protect against unauthorized actions.

#### **2. Role-Based Access Control**

- The platform uses role-based logic to control user access:
  - Customers can book events but cannot create or edit them.
  - Event holders can create, update, and delete their own events.
  - Admins have full access to all content and user data.

#### **3. Defensive Design**

- **Input Validation**:
  - Forms validate user input to ensure data integrity and avoid errors.
- **Error Handling**:
  - User-friendly error messages and fallback pages guide users when issues arise.
- **Restricted Access**:
  - Unauthenticated users are redirected to the login page when attempting to access restricted sections like event creation or bookings.

#### **4. Data Management**

- All user-generated content is tied to their `user_id`. Deletion of a user cascades and removes related data (e.g., bookings, events) to prevent orphaned records.
- Users can update or delete their profile information, but account deletion is currently unavailable. This will be included in a future release.

---

## **User View - Registered/Unregistered**

MusicMatch has been designed to offer a seamless experience for both registered and unregistered users. The following breakdown outlines the features accessible to each user type:

### **Feature Access**

| **Feature**   | **Unregistered User**                                                                | **Registered, Logged-In User**                  |
| ------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------- |
| **Home Page** | Visible                                                                              | Visible                                         |
| **Profile**   | Not Visible - "Profile" icon only appears for registered, logged-in users            | Visible with full feature interaction available |
| **Events**    | Visible but users cannot book tickets, "Book Now" redirects to the login/signup page | Visible with full feature interaction available |
| **Bookings**  | Not Accessible                                                                       | Visible with full CRUD functionality            |
| **Gallery**   | Visible but users cannot upload photos                                               | Visible with the option to upload photos        |
| **Visit Us**  | Visible with interactive map functionality                                           | Visible with the same features                  |

---

## **CRUD Functionality**

MusicMatch enables users to Create, Read, Update, and Delete data across various sections of the site. The table below provides a breakdown of CRUD functionality for each feature:

| **Feature**  | **Create**                              | **Read** | **Update**               | **Delete**                                     |
| ------------ | --------------------------------------- | -------- | ------------------------ | ---------------------------------------------- |
| **Profile**  | Automatically created upon registration | Yes      | Yes                      | Deletion tied to account removal (Admins only) |
| **Events**   | Yes (Event Holders only)                | Yes      | Yes (Event Holders only) | No (Admin Holders only)                        |
| **Bookings** | Yes                                     | Yes      | Yes                      | Yes                                            |
| **Gallery**  | Yes (Upload photos)                     | Yes      | No                       | Yes                                            |

---

## **Feature Showcase**

### **Header/Navigation & Footer**

#### **Header & Navigation**

- The navigation bar allows all users to move around the site easily.
- When logged in, customers will see exclusive functions for them, namely viewing all upcoming events and my bookings, whereas event holders will see my events and create an event
- Registered users will see a "Logout" feature, which is hidden from unregistered users.

![alt text](media/Header.png)

#### **Footer**

- The footer includes a simple copyright message to provide the site legitimacy.

![alt text](media/Footer.png)

---

### **Home Page**

- **Unregistered Users**: A "Register" button is prominently displayed in the navbar section, inviting new users to join the community. They are also sent to register links when they click on any buttons in the hero and features sections. Any buttons or links on the page redirect them to register an account.

![alt text](media/Features_Home.png)
![alt text](media/Hero_Home.png)

- **Registered Users**: A "Logout" in the navbar replaces the login and the register function is replaced with their respective event holder or customer functions.

---

### **Registration/Sign-Up**

- Users must enter their username, email, first name, last name, their role, and password.
- Users will be sent to their respective customer or event holder homepages after login.

![alt text](media/Register1.png)
![alt text](media/Login1.png)

---

### **Profile**

- **Registered Users**:
- In future iterations, profiles created upon registration and can be personalized with a display name, profile picture, and bio.

---

### **Events**

- **Unregistered Users**: Cannot view upcoming events, book tickets, create events, or see what events they have created
- **Registered Users**: Have full access to book events and manage their bookings if a customer.
- Event Holders can create, update, and delete events.

![alt text](media/Upcoming_Events1.png)
![alt text](media/Booked_Events1.png)

---

### **Bookings**

- **Registered Users Only**: Users can create, update, and delete bookings through the upcoming events and my bookings pages.
- **Feedback on Bookings**: Users receive instant feedback on the status of their bookings, being redirected to their bookings page with the selected event and no. of tickets.
- In future development, booking confirmations will include email notifications. I would also like to provide a unique ticket number or QR code that can be shown to hostees in person. This would make sense alongside payment integration to provide the site legitimacy.

![alt text](media/Create_Event1.png)
![alt text](My_Events1.png)

---

## **Admin Panel**

The Django Admin Panel gives administrators full control over all user-generated content:

- **Manage Users**: Admins can view and delete user accounts, which cascade-delete related bookings and events.
- **Approve Content**: Admins approve event submissions.
- **Handle Bookings**: Admins can manage bookings directly from the admin interface.

![alt text](media/Admin_Panel.png)

---

### **Future Development**

For future versions of MusicMatch, the following features will enhance its database schema and security:

1. **Payment Integration**:
   - Adding support for secure payment gateways (e.g., Stripe or PayPal) to process event ticket purchases.
2. **Feedback System**:
   - Users will be able to leave reviews for events and organizers.
3. **Enhanced User Authentication**:
   - Integration with social login options (e.g., Google or Facebook) via Django AllAuth.
4. **Advanced Search Filters**:
   - Adding search options for events based on `music_genre`, or `date` as two examples.
5. **Event Holder Event Management**:
   - Adding further functions for event holders based on `no. of attendees` or `changing event details` as two examples.

## **Technologies & Languages Used**

### **Languages**

- **HTML**: For the structure and content of the webpages.
- **CSS**: For styling and ensuring a visually appealing design.
- **Python**: The backend programming language used to build and manage the application.

### **Version Control & Collaboration**

- **Git**: Used for version control to manage changes to the codebase.
- **GitHub**: For online storage of the codebase and project management using the Projects tool.

### **Development Environment**

- **Gitpod**: A cloud-based development environment used for initial project setup and development.
- **Visual Studio Code (VS Code)**: Used as the primary local development environment for building and debugging the application.
- **Figma**: Used for designing wireframes and planning the visual layout of the website.
- **Coolors**: For creating the website’s color theme and checking color accessibility.

### **Frameworks & Libraries**

- **Django 4.2.18**: A Python-based framework used to build the web application.
- **Bootstrap v5.3**: For responsive front-end design and layout.

### **Cloud & Database Services**

- **Cloudinary**: For cloud storage of user-uploaded media such as images.
- **PostGRE SQL**: For hosting the PostgreSQL database that manages user and event data.
- **Heroku**: Used to host the deployed version of the MusicMatch application.

### **Design & Media Tools**

- **DALL-E**: For image creation and editing.

### **Accessibility & Testing**

- **WAVE**: For evaluating the accessibility of the site.
- **Lighthouse**: For performance and SEO testing of the site.

---

## **Tools & Programs**

- **Lucidchart**: For creating the Entity Relationship Diagram (ERD) used to visualize database relationships.
- **Microsoft Co-Pilot**: For coding errors.
- **ChatGPT**: for debugging.
- **Perplexity AI**: Used as a resource to break down complex Django concepts and documentation into digestible information.

---

# Deployment

## Connecting to GitHub

To begin this project from scratch, follow these steps:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Click **New** to create a new repository.
3. Name your repository (e.g., `MusicMatch`) and add a description.
4. Initialize the repository with a `README.md` file.
5. Clone the repository to your local development environment or IDE (e.g., Gitpod or VS Code).

---

## Django Project Setup

1. Install Django and required libraries:
   pip install 'django<4' gunicorn pip install dj_database_url psycopg2 pip install dj3-cloudinary-storage
2. Create a `requirements.txt` file to list all installed dependencies:
   pip freeze > requirements.txt
3. Start a new Django project and app:
   django-admin startproject musicmatch . python manage.py startapp events
4. Add the app to `INSTALLED_APPS` in `settings.py`:
   INSTALLED_APPS = [ ..., 'events', ]
5. Create a superuser to access the Django admin panel:
   python manage.py createsuperuser
6. Apply database migrations:
   python manage.py migrate
7. Create an `env.py` file to store sensitive environment variables:

```python
import os

os.environ["DATABASE_URL"] = "your_database_url_here"
os.environ["SECRET_KEY"] = "your_secret_key_here"
```

8. Update settings.py to use the env.py file:

```python
   import os
   import dj_database_url

if os.path.exists("env.py"):
import env

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
} 9. Set up the templates directory in settings.py:
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
{
...,
'DIRS': [TEMPLATES_DIR],
}
] 10. Create static, media, and templates directories in your project folder. 11. Add a Procfile for Heroku deployment:
web: gunicorn musicmatch.wsgi
```

## Cloning the Repository

1. Log in to [GitHub](https://github.com/).
2. Navigate to the repository and click the **Code** button.
3. Copy the HTTPS, SSH, or GitHub CLI URL.
4. Open your terminal and run the following command:
   ```bash
   git clone <https://github.com/mahmudurmahid/individual-full-stack-project>
   ```
5. Navigate to the cloned directory and install dependencies:
   pip install -r requirements.txt

## Forking the Repository

1. Log in to [GitHub](https://github.com/).
2. Navigate to the repository and click **Fork** (top-right corner).
3. You now have a copy of the repository in your GitHub account.
4. Clone and configure the forked repository by following the steps in the **Cloning the Repository** section.

## AI Tools in Development

### Using AI to Assist in Code Creation

Throughout the development of the MusicMatch project, AI tools like **ChatGPT** and **GitHub Copilot** were strategically utilized to streamline code creation and ensure alignment with project objectives. Key use cases include:

- **Feature Implementation:** AI was used to generate the initial structure for Django models, views, and serializers. For example, the AI-generated structure for the **Event** and **Booking** models significantly reduced development time and provided a solid foundation to build upon.
- **Reusable Components:** AI helped create reusable HTML templates and Bootstrap-based designs for the site, such as event cards and modals for bookings.
- **Challenges:** While AI-generated code often followed best practices, there were instances where the code lacked specific context for the project’s requirements, necessitating manual adjustments or complete rewrites.
- **Outcomes:** Despite occasional limitations, the AI-generated code improved development efficiency and offered a valuable starting point for feature implementation.

---

### Using AI to Assist in Debugging

AI tools played a vital role in identifying and resolving bugs during the development process. Examples include:

- **Bug Identification:** ChatGPT was used to analyze error messages, such as `AttributeError` or `DatabaseNotFoundError`, and provided step-by-step solutions to resolve these issues. For instance, AI flagged a missing database configuration in the `env.py` file, which was then quickly corrected.
- **Performance Fixes:** AI tools identified slow database queries and recommended the use of Django’s `select_related()` and `prefetch_related()` for optimizing query performance.
- **Challenges:** Occasionally, AI provided overly generic debugging advice or suggestions that didn’t directly apply to the specific problem, requiring additional effort to cross-check or refine the solution.
- **Outcome:** Debugging with AI significantly reduced development downtime, providing quick insights and actionable fixes for complex issues, even if some solutions required further refinement.

---

### Using AI to Optimize Code for Performance and UX

AI tools were instrumental in optimizing the codebase for better performance and user experience. Highlights include:

- **Code Optimization:** GitHub Copilot suggested optimized algorithms and cleaner code structures for functionalities like pagination and filtering events.
- **Responsive Design:** ChatGPT provided suggestions for Bootstrap classes and media queries to ensure the website’s responsiveness across different screen sizes.
- **User Feedback Enhancements:** AI recommended using tooltips and hover effects to improve the user experience. This was applied to icons in the navigation bar and interactive elements like buttons.
- **Challenges:** Some AI suggestions prioritized technical correctness but lacked awareness of the user experience or project-specific design goals. These suggestions had to be manually reviewed and adapted.
- **Outcome:** By integrating AI-driven suggestions, the project achieved faster load times, improved usability, and a more intuitive interface for users, though human oversight was essential for fine-tuning the optimizations.

---

### Using AI to Create Automated Unit Tests

To ensure robust testing, AI tools like GitHub Copilot were employed to generate Django unit tests for key application features:

- **Generated Tests:**
  - **Models:** Unit tests for validating model fields, relationships, and default values (e.g., `Event` and `Booking` models).
  - **Views:** Tests to verify user access to views based on authentication and permissions.
  - **Forms:** Validation tests to ensure proper error handling and feedback for incorrect user inputs.
- **Enhancements to AI-Generated Tests:**
  - Adjusted test logic to include edge cases, such as invalid booking dates or duplicate events.
  - Expanded test coverage to include scenarios not initially generated by AI, ensuring comprehensive validation.
- **Challenges:** AI occasionally produced incomplete or overly simplistic tests, which missed more nuanced scenarios, requiring additional manual intervention.
- **Outcome:** Copilot accelerated the creation of unit tests, saving time and ensuring a high level of test coverage, though manual adjustments were necessary for completeness and accuracy.

---

### Reflection on AI’s Role in the Development Process

AI tools like ChatGPT and GitHub Copilot significantly enhanced the efficiency and quality of the MusicMatch development process. However, the experience highlighted both the benefits and limitations of relying on AI:

- **Positive Impacts:**

  - **Efficiency Gains:** AI streamlined the development workflow by automating repetitive tasks, such as creating model methods, views, and test cases, allowing more time to focus on feature implementation and refinement.
  - **Problem-Solving:** AI acted as a reliable debugging assistant, quickly pinpointing errors and offering actionable solutions, which minimized downtime during development.
  - **Learning Opportunities:** AI served as a learning tool, explaining complex Django concepts, such as custom authentication backends and query optimizations, in a digestible format.

- **Challenges and Limitations:**

  - **Context Awareness:** AI occasionally lacked project-specific context, resulting in generic or misaligned code suggestions that required significant manual refinement.
  - **Test Coverage:** While AI-generated unit tests covered the basics, additional effort was needed to ensure coverage for edge cases and more complex scenarios.
  - **Over-Reliance Risk:** Over-reliance on AI for debugging or code generation could potentially reduce opportunities for deeper learning and problem-solving.

- **Overall Impact:** The integration of AI tools not only accelerated development but also improved the final product by optimizing performance, enhancing user experience, and ensuring robust test coverage. However, the need for human oversight and customization remained critical for achieving the desired outcomes.

---

## Testing

### Validation

#### Python Validation

I used **CI Python Linter** to check the Python files for compliance with PEP 8 standards. Below are the results and corresponding fixes:

| **File**    | **Line**   | **Issue**                            | **Fix Implemented**                                                             |
| ----------- | ---------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| `models.py` | 6          | E302 expected 2 blank lines, found 1 | Added blank lines to maintain proper spacing between class definitions.         |
|             | 26, 39, 48 | E501 line too long (> 79 characters) | Broke long lines into multiple lines using appropriate line breaks.             |
|             | 54, 59     | E302 expected 2 blank lines, found 1 | Added blank lines to separate functions and classes properly.                   |
| `views.py`  | Multiple   | E302, E501, W293                     | Adjusted spacing and broke long lines into shorter ones for better readability. |
|             | 56         | W293 blank line contains whitespace  | Removed trailing whitespace.                                                    |
| `forms.py`  | 7, 73, 92  | E302 expected 2 blank lines, found 1 | Added blank lines to improve spacing between class and function definitions.    |
|             | 43, 78, 95 | E501 line too long (> 79 characters) | Split overly long lines into multiple shorter lines.                            |
| `urls.py`   | 10         | E501 line too long (> 79 characters) | Broke long URL patterns into separate lines to comply with PEP 8.               |

#### Fix Implementation Summary

- **Spacing Issues (E302):** Fixed by ensuring two blank lines between top-level class and function definitions.
- **Line Length Issues (E501):** Fixed by wrapping long lines at appropriate breaking points.
- **Trailing Whitespace (W293):** Removed extra spaces to ensure a clean structure.

#### HTML Validation

The **W3C Validator** was used to validate HTML files. Below are the issues encountered and the fixes applied:

| **File**        | **Issue**                                                                                                  | **Fix Implemented**                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `index.html`    | Trailing slashes on void elements interact badly with unquoted attribute values.                           | Removed unnecessary trailing slashes from void elements like `<meta>` and `<link>`.                     |
|                 | Illegal character in `href` attributes using `{% url %}`.                                                  | Ensured `{% url %}` syntax is only interpreted in Django templates during rendering.                    |
| Other Templates | Parse errors on `{% load static %}` and unrecognized template tags like `{% for %}` and `{% if %}` blocks. | Verified these errors occur only because Django template tags aren't recognized in raw HTML validation. |

Examples of W3C Validator results:
![alt text](media/Screenshot_2025-01-27_at_09.50.59.png)
![alt text](media/Screenshot_2025-01-27_at_09.51.16.png)

#### CSS Validation

No errors or warnings were detected in the `style.css` file.
![alt text](media/Screenshot_2025-01-27_at_09.50.59.png)

---

### Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms accept the intended input, process it correctly, and provide appropriate feedback to users.

| **Feature**                | **Tested?** | **User Input Required**                          | **User Feedback Provided**                                                                                              | **Pass/Fail** | **Fix** |
| -------------------------- | ----------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------- | ------- |
| **Navbar**                 | Yes         | Click links in navbar                            | Navbar links take users to the intended locations (e.g., Home, Events, Bookings). Tooltips provide extra accessibility. | Pass          | -       |
| **Home Page Hero Section** | Yes         | Click buttons on hero section                    | Buttons redirect users to the login or events pages.                                                                    | Pass          | -       |
| **Register Form**          | Yes         | Email, username, password, first/last name, role | Validation for empty fields, email format, password length, and password confirmation provided.                         | Pass          | -       |
| **Login Form**             | Yes         | Email/username and password                      | Displays errors for incorrect credentials or empty fields.                                                              | Pass          | -       |
| **Create Event Form**      | Yes         | Text, date, dropdown for genre                   | Validation for required fields, invalid date input, and missing details.                                                | Pass          | -       |
| **Filter Events Form**     | Yes         | Dropdown selections for genre, city, and date    | Updates event list dynamically based on filter criteria or shows "No events found" message.                             | Pass          | -       |
| **Book Event Button**      | Yes         | Click "Book Now" button                          | Confirms booking and redirects user to "My Bookings" page.                                                              | Pass          | -       |
| **My Bookings Page**       | Yes         | Add/Remove ticket buttons                        | Users can adjust ticket count. Shows "Booking updated" message.                                                         | Pass          | -       |
| **Delete Booking Button**  | Yes         | Click "Delete" button                            | Prompts user for confirmation before deleting the booking.                                                              | Pass          | -       |
| **Edit Profile Form**      | Yes         | Update role or venue name                        | Updates user profile and redirects to home page with success message.                                                   | Pass          | -       |
| **Logout Button**          | Yes         | Click "Logout" button                            | Logs user out and redirects to login page.                                                                              | Pass          | -       |

---

### Testing User Stories

User stories were documented in the project board and tested on various screen sizes using Chrome DevTools. Multiple test accounts (e.g., `TestUser1`, `EventHolder1`) were created to ensure comprehensive coverage.

| **User Story**                | **Acceptance Criteria Met?** | **Tested?** | **Response**                                                                                      | **Pass/Fail** | **Fix** |
| ----------------------------- | ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------- | ------------- | ------- |
| **#1 - Register as a User**   | Yes                          | Yes         | User can register as a "Customer" or "Event Holder." Validation feedback provided for all inputs. | Pass          | -       |
| **#2 - Log in as a User**     | Yes                          | Yes         | User can log in using valid credentials. Errors displayed for invalid inputs.                     | Pass          | -       |
| **#3 - View Events List**     | Yes                          | Yes         | Events list shows upcoming events with filters for genre, city, and date.                         | Pass          | -       |
| **#4 - Book an Event**        | Yes                          | Yes         | Booking is added, and the user is redirected to the "My Bookings" page.                           | Pass          | -       |
| **#5 - Manage Bookings**      | Yes                          | Yes         | User can add/remove tickets or delete bookings.                                                   | Pass          | -       |
| **#6 - Create an Event**      | Yes                          | Yes         | Event Holder can create events with all required details.                                         | Pass          | -       |
| **#8 - Logout Functionality** | Yes                          | Yes         | User is logged out and redirected to the login page.                                              | Pass          | -       |
| **#9 - Responsive Design**    | Yes                          | Yes         | Website is fully functional and accessible on desktop, tablet, and mobile screens.                | Pass          | -       |

---

#### Device Testing

The site was tested on the following devices for responsiveness:

- Desktop: Chrome, Firefox, Safari
- Mobile: iPhone (Safari), Android (Chrome)

#### Browser Compatibility

The application was verified to work on the following browsers:

- Google Chrome (latest)
- Mozilla Firefox (latest)
- Safari (iOS)

#### Accessibility

The site was checked for basic accessibility using browser dev tools to ensure proper color contrast and screen reader support. Using the WAVE Accessibility Evaluation tool, I found the following results:
![alt text](media/Screenshot_2025-01-27_at_14.07.35)

While the WAVE Accessibility Evaluation tool has identified contrast errors and six additional alerts, the current design prioritizes maintaining the website's cohesive visual identity. These alerts do not indicate outright accessibility violations but rather areas for potential enhancement. Moving forward, we are committed to refining our design to better align with accessibility standards while preserving the platform’s aesthetic and branding goals. In the interim, users can leverage browser tools or assistive technologies to further optimize their experience.

#### Solved Bugs

As this was my first Django project incorporating database relationships, most bugs encountered were related to learning and understanding the framework. Below is a list of key bugs that required extended investigation or assistance to resolve:

| **No.** | **Bug**                                                                                                       | **Solved?** | **Fix**                                                                                                                               | **Solution Credit**            |
| ------- | ------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 1       | CSRF token errors during form submissions in deployed Heroku app.                                             | Yes         | Correctly added `{% csrf_token %}` in all forms and ensured `CSRF_TRUSTED_ORIGINS` was configured in `settings.py`.                   | Django Docs                    |
| 2       | Errors with the role-based redirection for users after login (customers vs. event holders).                   | Yes         | Adjusted the `login_view` to redirect users based on their role by querying the `Profile` model.                                      | ChatGPT + Django Documentation |
| 3       | Static files (CSS and images) not loading correctly in the deployed app.                                      | Yes         | Configured `STATIC_ROOT` and ensured the `collectstatic` command was executed properly on deployment to Heroku.                       | StackOverflow + Django Docs    |
| 4       | Bootstrap modal closing error in the browser console: `Uncaught TypeError: Cannot read properties of null...` | Yes         | Updated the Bootstrap library to the latest version and ensured modal scripts were correctly included in the base template.           | Bootstrap Documentation        |
| 5       | Adding tickets beyond a specific number caused database errors for bookings.                                  | Yes         | Added validation in the `remove_ticket` and `add_ticket` views to ensure `ticket_count` stayed within a valid range (>= 0).           | ChatGPT                        |
| 6       | Carousel images not displaying in the deployed version of the site.                                           | Yes         | Updated `MEDIA_URL` and ensured Cloudinary was configured correctly to store and serve image assets for deployment.                   | Cloudinary Documentation       |
| 7       | Events created by a host not showing up under "My Events."                                                    | Yes         | Fixed the queryset in the `my_events` view to correctly filter events by the logged-in organizer.                                     | ChatGPT + Django Documentation |
| 8       | Placeholder images not displaying on user profiles if no custom image was uploaded.                           | Yes         | Added a default image URL in the `Profile` model and updated the template logic to handle missing profile images gracefully.          | Django Docs                    |
| 9       | Bookings not being deleted when a user was removed.                                                           | Yes         | Set `on_delete=models.CASCADE` for the `user` ForeignKey in the `Booking` model to ensure related bookings are deleted with the user. | Django Documentation           |

These bugs provided an excellent learning opportunity and helped me deepen my understanding of Django, database management, and deployment challenges.

#### Known Bugs

1. **Placeholder Text Issue on Booked Events Page**
   - **Description:** On the `booked_events.html` page, the placeholder `{{ booking.event.city }}` is displayed instead of the actual city name for a booked event.
   - **Impact:** This affects the display of the event address, which may confuse users.
   - **Root Cause:** The placeholder text is not being correctly replaced with the actual value from the database. This could be due to a missing or incorrect reference in the context data passed to the template.
   - **Plan to Fix:** I will review the `booked_events` view and ensure the `city` field is properly included in the context. Additionally, I will test the template to confirm the variable is correctly rendered in all scenarios.

---

## Credits

### Code

The following resources, blogs, and tutorials were instrumental in helping me build this project:

- **Django Documentation**: For understanding the MVT framework, working with forms, models, and user authentication.
  - [Django Documentation](https://docs.djangoproject.com/en/stable/)
- **Bootstrap Documentation**: For creating a responsive and visually appealing front-end.
  - [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- **Django Models and Relationships**: Helped with designing models and implementing ForeignKey and OneToOne relationships.
  - [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- **Django Class-Based Views**: Used for implementing views efficiently.
  - [Django Class-Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
- **Django Forms**: Provided guidance for creating forms and handling validations.
  - [Django Forms](https://docs.djangoproject.com/en/stable/topics/forms/)
- **Django Signal Handlers**: Used for creating `post_save` signals in the `Profile` model.
  - [Django Signals](https://docs.djangoproject.com/en/stable/ref/signals/)
- **Django QuerySet API**: For filtering, querying, and optimizing database interactions.
  - [Django QuerySet API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- **Django Admin Customization**: Helped customize the admin panel for `Event`, `Booking`, and `Profile` models.
  - [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- **Static and Media Files in Django**: For configuring static files and media uploads with Cloudinary.
  - [Django Static Files](https://docs.djangoproject.com/en/stable/howto/static-files/)
- **Cloudinary for Media Storage**: Used to set up media storage for user-uploaded files.
  - [Cloudinary Documentation](https://cloudinary.com/documentation/django_integration)
- **Whitenoise for Serving Static Files**: Simplified serving static files in production.
  - [Whitenoise Documentation](http://whitenoise.evans.io/en/stable/)
- **Heroku Deployment for Django Apps**: Helped with deploying the project to Heroku.
  - [Deploying Django Apps on Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
- **PostgreSQL Setup for Django**: Assisted in configuring the PostgreSQL database for production.
  - [Django PostgreSQL Setup](https://docs.djangoproject.com/en/stable/ref/databases/#postgresql-notes)
- **Django AllAuth**: For exploring future social login integration.
  - [Django AllAuth](https://django-allauth.readthedocs.io/en/stable/installation.html)
- **Error Handling in Django**: Helped create custom error pages for 404 and 500 errors.
  - [Custom Error Pages](https://docs.djangoproject.com/en/stable/howto/error-reporting/)
- **StackOverflow**: For resolving various issues with Django settings, debugging, and deployment.
  - [StackOverflow](https://stackoverflow.com/)
- **W3Schools**: For basic HTML, CSS, and JavaScript references.
  - [W3Schools](https://www.w3schools.com/)
- **Lucidchart**: Used to create the Entity Relationship Diagram (ERD) to visualize database relationships.
  - [Lucidchart](https://www.lucidchart.com/)
- **ChatGPT**: Provided support for debugging, optimizing, and generating code throughout various stages of the project.
- **Microsoft Co-Pilot**: Assisted with code suggestions, debugging, and optimization during development.
- **Amy CI Course Instructor (Github)**: Provided insights on building Django projects like booking and scheduling systems, and I heavily relied upon her readme for my own.
  - [Amy’s Repository](https://github.com/amylour/FreeFido_v2/blob/main/README.md)

### Media

The following resources provided the media and visuals used in this project:

- **DALL-E**: For creating project-specific images and design elements.
- **Balsamiq**: Used to design custom wireframes.
- **Coolors**: Used for creating the color palette and ensuring accessibility.

### Acknowledgements

- **Code Institute Community**: For feedback, guidance, and motivation during the development process.
- **My Mentor (Amy)**: For their invaluable advice and constructive suggestions throughout the project.
- **Friends and Family**: For assisting with testing and providing feedback to improve the site.
- **Perplexity AI**: Helped break down complex Django concepts and debug specific challenges in the project.
- **Tutor Support**: For assisting with complex bugs, including deployment challenges, debugging logic, and understanding Django best practices.

### Additional Reading/Tutorials

- **Python Crash Course** by Eric Matthes: A helpful guide to understanding Python fundamentals.
  - [Python Crash Course](https://nostarch.com/python-crash-course)
- **GeeksforGeeks**: For explaining Django's ORM, class-based views, and template filtering.
  - [GeeksforGeeks Django](https://www.geeksforgeeks.org/django-tutorial/)
- **Django for Beginners** by William S. Vincent: A beginner-friendly book for understanding Django.
  - [Django for Beginners](https://djangoforbeginners.com)
- **W3Schools**: For guidance on HTML, CSS, and JavaScript concepts and syntax.
  - [W3Schools](https://www.w3schools.com/)
