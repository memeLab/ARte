# 1. Introduction

This vision document aims to present the project in its context of existence, as well as an overview of some aspects of the product in order to understand its objectives, opportunities, problems that it aims to solve and other related issues.

This document is a contribution from students allocated to the Jandig group in the discipline of Software Configuration and Evolution Management, from the Software Engineering course of the first semester of 2020 at the University of Brasília, Campus Gama.

## 1.1. Scope

This project aims to develop a responsive web application in order to create works of art with Augmented Reality (AR) technology, aiming to make it possible to hold Exhibitions of such arts, in order to reach a different audience and with a more technological look, in addition to making you an active participant in the creation of artistic elements.

The project invites the public to transcend the common Exhibition space, so that it can be viewed in a range of media, as long as the basic requirements are met.

## 1.2 Definitions, acronyms and abbreviations
The definitions, acronyms and abbreviations of the terms used in this document will be listed in this topic, in order to facilitate the understanding of the public interested in the project.

# 2. Positioning
## 2.1 Business opportunity

The opportunity was identified to unite artists and the public in Exhibitions in a more simplified way through the application of augmented reality Jandig ARte. With this, artists can publish content through bookmarks and the public, with a camera device, can make their reading animated directly on the screen of their smartphone.

This application contributes to social events, fosters culture, attracts users and gives them autonomy to disseminate their content in a fun way with augmented reality.

## 2.2 Problem description

| The problem is | that affects | whose impact is | a successful solution would include |
| -------- | -------- | -------- | -------- |
| The difficulty in centralizing the dissemination of content by augmented reality | users, both artists and the public | the possible departure from this form of interaction between artist and audience | user engagement to publish and read augmented reality content right from an application |

## 2.3 Description of product position

The product can position itself as an easy-to-use online platform capable of engaging users, both artists and audiences, at events and Exhibitions. In addition to being an attractive way to disseminate and show content, it can be used as a vehicle for various information. 

## 3. Users description and their needs

## 3.1 Envolved parties summary

| Name | Description | Responsibilities |
| --- | --- | --- |
| memeLab | Laboratory for unstable media (company) | Creator of the product known as Jandig, as well as being one of its stakeholders |
| LabArteMidia - USP | Laboratório de Arte, Mídia e Tecnologias Digitais - University of Sao Paulo | Stakeholder for software development and content creation |
| Developers | Collaborators | Plan, design, prototype, develop, release and maintain Jandig |

## 3.2 Users description

| Name | Description |
| -------- | -------- |
| Artists | Professionals or laymen who wish to publish their works |
| Public | Art or technology lovers who want to see Artworks in different media, as well as co-create others, beyond the general public who want to interact with these Artworks through technology |

## 3.3 Main User Needs

| User | Needs | Proposed solution |
| -------- | -------- | -------- |
| Artist | Post and publicize your animated Artworks | PWA Application that allows adding and making material available to the public, in the form of Markers and animations |
| Public | Interact with bookmarks and read animations in augmented reality | Reading and interaction of ArtworkS through a PWA application |

## 3.4 User Environment
Users can fully use the application through browsers on their mobile devices, using the camera.

## 3.5 Users profiles

### 3.5.1 Artists

| Representatives | Type | Responsibility | Sucess Criteria | Involvement|
| - | - | - | - | - |
| Artists | Artistic community (includes independent artists, studios, organizations) | Produce art pieces that can be scanned by Jandig, disseminating theis pieces | Being able to utilize Jandig as a tool for AR-based Exhibitions | High |

### 3.5.2 Public

| Representatives | Type | Responsibility | Sucess Criteria | Involvement|
| - | - | - | - | - |
| Art viewers and appreciators | Art enthusiasts and other appreciators that would like to access their favorite pieces in a different manner | Appreciate and disseminate art pieces created using the Jandig tool | Viewing and interacting with Exhibitions and pieces | Medium |

# 4. Product overview

## 4.1 Product perspective

The Jandig initiative aims to bring about a new way of artcrafting, by means of using Augmented Reality technology as a displaying method, one that can be interacted with, with some limitations.

By enabling artists to create AR pieces, Jandig paves way for art to be less restricted to physical Exhibitions and/or museuns, but at the same time not excluding any of them. Jandig pieces can be attached to many surfaces, in which the user can simply open its website and read the specific piece to be able to see more of its contents.

Jandig also enable users to create their own Artworks and Exhibitions, following the same methods that professional artists use to create their Artworks on this platform. By doing so, art can become a subject that is less tied to professional artists, and more to the non-professional public.

## 4.2 Capabilities summary

| Benefits to the user | Support features |
| - | - |
| Ease of creating augmented reality Artworks | The application allows users and artists to create their art by providing an image and a .gif or video. The system will then provide the steps and other files and configurations that are required to create Artworks and Exhibitions. |
| Ease of viewing and interacting with Exhibitions | For the system to work and for the public to be able to use it, a smartphone with internet access and a camera are required. The user will connect to the platform through its specific URL and will be prompted by a page that asks to fire up the camera. By doing so and by selecting the Exhibition that is tied to the Artwork, users can then see through their smartphones camera the animation or video that is played in a loop.| 

## 4.3 Assumptions and dependencies

- The user needs to have access to a smartphone with a built-in camera and internet access.

- The responsive web app will be utilized by people that desire to see AR Artworks that were made within the app requirements.

# 5. Product requirements

| Identifier | Requirements |
| - | - |
| RF01 | Allow the user to create, edit, delete their account and log out |
| RF02 | Allow the user to recover their password |
| RF03 | Allow the user to choose the language option between English and Portuguese |
| RF04 | Allow the artist to upload an image to be used as a Marker on the platform |
| RF05 | Allow the artist to upload a Marker to the platform and allow it to be edited |
| RF06 | Allow the artist to upload an Object to the platform and allow it to be edited |
| RF07 | Allow the artist to create a Jandig Artwork |
| RF08 | Allow the artist to delete and edit a Artwork of his own |
| RF09 | Allow the artist to create a digital Exhibition |
| RF10 | Allow the artist to delete and edit an Exhibition of his own |
| RF11 | Allow the artist to see their own Markers, Objects, Artworks and Exhibitions |
| RF12 | Allow the artist to download your Markers, Objects, Artwork and Exhibitions |
| RF13 | Allow the user to see the entire collection of Objects, Markers, Artwork and Exhibitions published by anyone and also download any item in the collection |
| RF14 | Provide a space with tips for the user to learn more about the platform's operation, and allow them to search for some content by keywords |
| RF15 | Allow the user to choose which Exhibition they want to interact with |
| RF16 | Allow the user (with optional login) to interact with Exhibitions using the camera on a mobile device |  
