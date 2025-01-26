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
   - [Must-Have Features ✅](#must-have-features-)
   - [Should-Have Features ⏳](#should-have-features-)
   - [Could-Have Features 🚀](#could-have-features-)
6. [Scope Plane](#scope-plane)

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

![alt text](image.png)

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

## Scope Plane

| Feature               | Visitors | Registered Users |
| --------------------- | -------- | ---------------- |
| View Events           | Yes      | Yes              |
| Book Tickets          | No       | Yes              |
| Host Dashboard        | No       | Yes (Hosts Only) |
| Mobile Responsiveness | Yes      | Yes              |
| CRUD Functionality    | No       | Yes              |
