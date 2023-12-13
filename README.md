# SamuelGifford_T2A2 - API Web Server

![MoodNest](/docs/Moodnest.png)

### R0 - Introduction

*MoodNest* is a comprehensive and user-centric mental health check-in platform designed to address the growing need for accessible tools for daily mental well-being management. With a focus on proactive mental health, *MoodNest* aims to empower individuals to reflect on their mental well-being, track their emotions, and develop strategies for self-care. By providing a stigma-free environment and fostering a culture of openness, *MoodNest* strives to contribute to a healthier and more resilient society that prioritizes mental well-being.

---

## Table of Contents

* [R1 - Identification of the problem you are trying to solve by building this particular app](#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)
* [R2 - Why is it a problem that needs solving?](#r2---why-is-it-a-problem-that-needs-solving)
* [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
* [R4 - Identify and discuss the key functionalities and benefits of an ORM](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)
* [R5 - Document all endpoints for your API](#r5---document-all-endpoints-for-your-api)
* [R6 - An ERD for your app](#r6---an-erd-for-your-app)
* [R7 - Detail any third party services that your app will use](#r7---detail-any-third-party-services-that-your-app-will-use)
* [R8 - Describe your project's models in terms of the relationships they have with each other](#r8---describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
* [R9 - Discuss the database relations to be implemented in your application](#r9---discuss-the-database-relations-to-be-implemented-in-your-application)
* [R10 - Describe the way tasks are allocated and tracked in your project](#r10---describe-the-way-tasks-are-allocated-and-tracked-in-your-project)


---

### R1 - Identification of the problem you are trying to solve by building this particular app.
In the contemporary landscape, mental health has emerged as a critical facet of overall well-being, with an increasing global awareness of the huge impact of mental health challenges on individuals and societies. The problem at hand revolves around the substantial gap between the prevalence of mental health concerns and the accessibility of effective tools for daily mental well-being check-ins and management.  *MoodNest* endeavours to address this multifaceted challenge by providing a comprehensive and user-centric mental health check-in platform.

Global statistics underscore the gravity of mental health challenges. According to the World Health Organization (WHO), over 450 million people worldwide suffer from mental health disorders! Making mental health conditions a leading cause of ill-health and disability globally. Despite the staggering prevalence, a massive proportion of individuals do not have easy access to personalised and supportive platforms for regular mental health check-ins. 

A critical aspect of the problem lies in the underutilization of available mental health services. According to the Australian Institute of Health and Welfare (AIHW), nearly 65% of Australians with mental health disorders did not access mental health services in 2020. Stigma, lack of awareness, and societal attitudes continue to hinder individuals from seeking necessary support. *MoodNest* endeavours to challenge this underutilization by providing an Australian-centric, stigma-free environment that encourages individuals to engage in daily reflections on their mental well-being.

The workplace is a significant arena for mental health challenges in Australia as well. Work-related stress has been identified as a prominent issue affecting productivity. A study by *BeyondBlue*, an Australian mental health organization, reveals that work-related stress costs the Australian economy over $10 billion per year. The demanding nature of work environments, exacerbated by factors such as remote work and job uncertainty, underscores the need for targeted strategies. *MoodNest* acknowledges the impact of workplace stress on mental health and productivity, positioning itself as a valuable reDocumentation for Australians seeking daily strategies to manage stress and achieve a healthier work-life balance.

Young Australians are particularly vulnerable to mental health challenges, and the statistics emphasize the urgency of targeted interventions. According to the ABS, mental health conditions are prevalent among young Australians, with around 26% of people aged 16 to 24 experiencing mental health disorders. 

---

### R2 - Why is it a problem that needs solving?

The imperative to address mental health challenges through the development of *MoodNest* stems from a profound understanding of the gravity and far-reaching implications of unmet mental health needs within the Australian population. The necessity to solve this problem is underscored by several compelling reasons that highlight the societal, economic, and individual impact of untreated mental health concerns.

1. **Burden on Individuals and Families:**
   - Mental health challenges can exert a significant toll on individuals and their families. Untreated conditions may lead to prolonged suffering, strained relationships, and diminished quality of life. By not providing accessible and proactive mental health tools, we risk perpetuating a cycle of silent suffering and preventable distress.

2. **Economic Impact:**
   - Mental health issues exact a considerable economic toll on Australia. Workplace stress, unaddressed mental health concerns, and the associated productivity losses cost the economy billions annually. Addressing mental health concerns through *MoodNest* can contribute to a more resilient and productive workforce, thereby mitigating these economic losses.

3. **Social and Emotional Well-being:**
   - Mental well-being is intrinsic to overall health and happiness. By not addressing mental health concerns, individuals may face challenges in sustaining positive social connections and emotional equilibrium. *MoodNest* aims to enhance social and emotional well-being by providing tools for daily reflection and proactive mental health management.

4. **Preventive Approach to Mental Health:**
   - The traditional healthcare model often emphasizes intervention after the onset of acute mental health issues. *MoodNest* seeks to shift this paradigm by fostering a preventive approach. By empowering individuals with daily tools for self-reflection and proactive management, the app aims to curb the escalation of mental health concerns before they reach crisis levels.

5. **Reducing Stigma and Barriers to Access:**
   - Stigma and a lack of awareness continue to hinder individuals from seeking mental health support. *MoodNest* strives to be part of the solution by providing a stigma-free environment, encouraging individuals to engage in daily reflections without fear of judgment. By reducing these barriers, *MoodNest* promotes a culture of openness and acceptance around mental health.

6. **Youth Empowerment and Resilience:**
   - Young Australians face unique stressors, and mental health challenges during this critical period can have long-lasting effects. *MoodNest's* focus on youth engagement is crucial for instilling healthy mental health habits early on, empowering the younger generation to navigate life's challenges with resilience and self-awareness.

7. **Post-Pandemic Mental Health Landscape:**
   - The ongoing impact of the COVID-19 pandemic has heightened mental health concerns globally, including in Australia. *MoodNest* recognizes the need for responsive tools to navigate the post-pandemic mental health landscape. Addressing the emotional fallout from the pandemic is crucial for individual and collective recovery.

8. **Strategic ReDocumentation Allocation:**
   - By addressing mental health concerns through *MoodNest*, there is an opportunity to strategically allocate reDocumentations. Proactive mental health management can potentially alleviate the burden on traditional healthcare services, allowing for more efficient reDocumentation utilization and a more equitable distribution of mental health support.

In conclusion, the problem of untreated mental health challenges in Australia is multifaceted, affecting individuals, families, workplaces, and society at large. *MoodNest's* significance lies in its commitment to addressing these challenges head-on by providing a comprehensive and user-centric solution. By doing so, *MoodNest* aims to contribute to a healthier, more resilient, and compassionate society that prioritizes the mental well-being of its individuals.

---

### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

In choosing PostgreSQL as the preferred database system, several factors were taken into account, each contributing to its selection for specific reasons. However, it's crucial to acknowledge potential drawbacks compared to other options, such as MySQL.

### Reasons for Choosing PostgreSQL:

1. **Advanced Features:** PostgreSQL's object-relational nature, table inheritance, and function overloading provide advanced features that align with the project's requirements. These features enhance the flexibility and modelling capabilities of the database.

2. **Concurrency Handling:** PostgreSQL's implementation of Multi version Concurrency Control (MVCC) without read locks, support for parallel query plans, and non-blocking index creation contribute to efficient concurrency handling. This is particularly advantageous for scenarios with simultaneous read and write operations.

3. **SQL Standards Compliance:** PostgreSQL closely adheres to SQL standards, ensuring compatibility and consistency in query execution. This adherence simplifies the development process and promotes best practices.

4. **Data Integrity at Transaction Level:** PostgreSQL's commitment to data integrity at the transaction level makes it a robust choice, minimising vulnerabilities to data corruption and ensuring the reliability of stored information.

5. **Extensibility:** The high extensibility of PostgreSQL, supporting a variety of advanced data types and allowing the addition of custom data types, operators, and index types, aligns well with the project's need for versatility.

6. **Open-Documentation Nature:** PostgreSQL being truly open-Documentation and community-driven ensures transparency, community support, and continuous improvement. It aligns with the project's commitment to open-Documentation principles.

### Drawbacks Compared to Others, Such as MySQL:

1. **Popularity and Ecosystem:** PostgreSQL is less popular than MySQL, resulting in a smaller ecosystem of third-party tools and a potentially smaller pool of available developers and administrators. This might impact the availability of reDocumentations and community support.

2. **ReDocumentation Consumption:** PostgreSQL forks a new process for each client connection, allocating a non-trivial amount of memory (about 10 MB per process). This can lead to higher reDocumentation consumption compared to databases like MySQL, which may impact scalability in certain scenarios.

3. **Read-Heavy Workloads:** For simple, read-heavy workflows, where speed is a higher priority than some advanced features, PostgreSQL might be perceived as a less optimal choice compared to MySQL. MySQL has historically excelled in read-heavy scenarios.

4. **Familiarity and Comfort:** The choice of PostgreSQL may pose a challenge in environments where MySQL is more familiar and comfortable for developers. Overcoming the learning curve associated with a less familiar database system could be considered a drawback.

In conclusion, while PostgreSQL was selected for its advanced features, strong concurrency handling, and adherence to SQL standards, it's essential to acknowledge potential drawbacks, including ecosystem considerations, reDocumentation consumption, and challenges in environments where MySQL is more prevalent. The decision to prioritize advanced features and data integrity influenced the selection, accepting trade-offs in areas where PostgreSQL might be perceived as less advantageous.


Documentations:

https://developer.okta.com/blog/2019/07/19/mysql-vs-postgres

---

### R4 - Identify and discuss the key functionalities and benefits of an ORM

An Object-Relational Mapping (ORM) is a powerful tool that facilitates the interaction between a relational database and the application code by abstracting the database operations into a higher-level, object-oriented paradigm. The key functionalities and benefits of an ORM include:

### Key Functionalities:

1. **Object-Oriented Model:**
   - **Benefit:** ORM allows developers to work with a more natural and intuitive object-oriented model in the programming language of their choice (e.g., Python, Java, C#).

2. **Entity Mapping:**
   - **Benefit:** ORM provides mechanisms to map application domain objects to corresponding database entities, streamlining the process of database interaction.

3. **CRUD Operations:**
   - **Benefit:** ORM frameworks automate the generation of standard CRUD (Create, Read, Update, Delete) operations, reducing the amount of boilerplate code developers need to write.

4. **Query Language:**
   - **Benefit:** ORM frameworks often come with a high-level query language that allows developers to express database queries using the programming language rather than raw SQL.

5. **Transaction Management:**
   - **Benefit:** ORM systems provide transaction management to ensure that multiple database operations can be grouped into atomic transactions, ensuring data consistency.

6. **Schema Generation:**
   - **Benefit:** ORM can automatically generate database schemas based on the application's object model, eliminating the need for manual schema definition in the database.

7. **Caching:**
   - **Benefit:** Some ORM frameworks include caching mechanisms, reducing the need for repeated database queries and improving application performance.

### Benefits:

1. **Abstraction of Database Complexity:**
   - **Benefit:** ORM shields developers from the intricacies of database-specific SQL syntax and intricacies, allowing them to focus on business logic.

2. **Improved Productivity:**
   - **Benefit:** By automating common database operations and providing an object-oriented interface, ORM frameworks increase developer productivity, enabling faster application development.

3. **Database Agnosticism:**
   - **Benefit:** ORM facilitates the development of database-agnostic applications. Developers can switch between different database systems with minimal code changes.

4. **Code Reusability:**
   - **Benefit:** ORM promotes code reusability by encapsulating database interactions in a reusable and modular form, making it easier to maintain and extend applications.

5. **Reduced SQL Injection Risk:**
   - **Benefit:** ORM frameworks typically use parameterized queries, reducing the risk of SQL injection attacks compared to manually constructed SQL queries.

6. **Portability:**
   - **Benefit:** Applications developed with ORM can be more easily ported across different platforms and environments due to the abstraction provided by the ORM layer.

7. **Easier Maintenance:**
   - **Benefit:** ORM facilitates easier maintenance by providing a clear separation between the application's business logic and the database interaction code.

In conclusion, an ORM simplifies the interaction between application code and relational databases, offering key functionalities such as object-oriented modeling, automated CRUD operations, and query languages. The benefits include increased productivity, abstraction of database complexities, and improved code maintainability.

---

### R5 - Document all endpoints for your API

### Table of Contents [Moodnest-Endpoints]

#### User Endpoints

1. [Register](#1-register)
2. [Login](#2-login)
3. [Get ALL users](#3-get-all-users)
4. [Delete User](#4-delete-user)
5. [Get User Stats](#5-get-user-stats)
6. [Change User Details](#6-change-user-details)

#### Mood Entry Endpoints

1. [Create Mood Entry](#1-create-mood-entry)
2. [Get All Mood Entries](#2-get-all-mood-entries)
3. [Get Specific Mood Entry](#3-get-specific-mood-entry)
4. [Update Mood Entry](#4-update-mood-entry)
5. [Delete Mood Entry](#5-delete-mood-entry)
6. [Get Depression Warning](#6-get-depression-warning)

#### Thought Journal Endpoints

1. [Create Thought Journal Entry](#1-create-thought-journal-entry)
2. [Get All Thought Journals](#2-get-all-thought-journals)
3. [Update Thought Journal](#3-update-thought-journal)
4. [Delete Thought Journal](#4-delete-thought-journal)

#### Goals Endpoints

1. [Create Goal](#1-create-goal)
2. [Get All Goals](#2-get-all-goals)
3. [Update Goal](#3-update-goal)
4. [Delete Goal](#4-delete-goal)

#### Activity Log Endpoints

1. [Create Activity Log](#1-create-activity-log)
2. [Get All Activity Logs](#2-get-all-activity-logs)
3. [Update Activity Log](#3-update-activity-log)
4. [Delete Activity Log](#4-delete-activity-log)

---


#### User Endpoints


## 1. Register
   - **Endpoint:**
      - **URL:** `/register`
      - **Method:** POST
      - **Auth:** None Required
   - **Description:** The `/register` endpoint allows users to sign up by providing registration information. No authentication is required, and successful registration results in the creation of a new user account. If the provided email is already in use, a conflict error is returned.
   - **Expected Responses:**
      - **Success (201 Created):**
         - Status Code: 201
         - Body: JSON containing the user's name, email, and a success message.
      - **Conflict (409):**
         - Status Code: 409
         - Body: JSON with an error message indicating that the provided email is already in use.

![Register_endpoint](/docs/Register_User.png)
![Register_endpoint](/docs/Email_in_use.png)
---


## 2. Login
   - **Endpoint:**
      - **URL:** `/login`
      - **Method:** POST
      - **Auth:** email, password
   - **Description:** The `/login` endpoint enables users to authenticate by providing their email and password. A successful login returns a JWT token, allowing access to protected routes. If the credentials are invalid, an error message is returned.
   - **Expected Responses:**
      - **Success (200 OK):**
         - Status Code: 200
         - Body: JSON containing the access token and user information.
      - **Unauthorized (401):**
         - Status Code: 401
         - Body: JSON with an error message indicating invalid email or password.

![login_endpoint](/docs/succesful_login.png)
![login_endpoint](/docs/failed_login.png)
---

## 3. Get ALL users
   - **Endpoint:**
      - **URL:** `/users`
      - **Method:** GET
      - **Auth:** JWT Token (Required), (ADMIN ONLY)
   - **Description:** Retrieves information for all users. Authentication with a valid JWT token is required, and only administrators have access to this endpoint. Returns a JSON array containing user data, including email, ID, admin status, name, registration date, and the latest mood entry emotion (if available).
   - **Expected Responses:**
      - **Success (200 OK):**
         - Status Code: 200
         - Body: JSON array containing user data.
      - **Forbidden (403):**
         - Status Code: 403
         - Body: JSON with an error message indicating that only administrators have access.

![get_all_users_endpoint](/docs/admin_Get_all_users.png)
![get_all_users_endpoint](/docs/admin_required_users.png)
---

## 4. Delete User
   - **Endpoint:**
     - **URL:** `/users/{user_id}`
     - **Method:** DELETE
     - **Auth:** JWT Token (Required), (ADMIN ONLY)
   - **Description:** Deletes a user account. Authentication with a valid JWT token is required, and only administrators have access to this endpoint. Deletes the specified user from the database. Returns a success message if the deletion is successful.
   - **Parameters:**
     - `{user_id}` (int): ID of the user to be deleted.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
   - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified user was not found.
   - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating that only administrators have access.


![delete_users_endpoint](/docs/delete_success.png)
![delete_users_endpoint](/docs/delete_user_not_found.png)
![delete_users_endpoint](/docs/delete_admin_required.png)
---

## 5. Get User Stats
   - **Endpoint:**
     - **URL:** `/users/{user_id}/stats`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves statistics for a specific user. Authentication with a valid JWT token is required. Users can only view their own stats. Returns the number of mood entries, goals, activity logs, and thought journals associated with the user.
   - **Parameters:**
     - `{user_id}` (int): ID of the user to retrieve stats for.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with user statistics.
   - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating that the user is not authorized to view these stats.

![user_stats_endpoint](/docs/user_status_success.png)
![user_stats_endpoint](/docs/user_stats_unauth.png)
---

## 6. Change User Details
   - **Endpoint:**
     - **URL:** `/users/{user_id}/change`
     - **Method:** PATCH
     - **Auth:** JWT Token (Required)
   - **Description:** Updates user details, including email and password. Users can only update their own details, while administrators can update any user's details. Returns a success message if the update is successful.
   - **Parameters:**
     - `{user_id}` (int): ID of the user to change details for.
   - **Request Body:**
     - JSON with the following optional fields:
       - `email` (string): New email address.
       - `password` (string): New password.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
     - **Conflict (409):**
       - Status Code: 409
       - Body: JSON with an error message indicating that the new email address is already in use.
     - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating that the user is not authorized to change these details.

![change_user_details_endpoint](/docs/change_successful.png)
![change_user_details_endpoint](/docs/change_email_in_use.png)
![change_user_details_endpoint](/docs/change_admin_required.png)
---

#### Mood Entry Endpoints

## 1. Create Mood Entry

   - **Endpoint:**
     - **URL:** `/mood_entries`
     - **Method:** POST
     - **Auth:** JWT Token (Required)
   - **Description:** Creates a new mood entry for the authenticated user. Requires a valid JWT token for authentication. The request body should contain information about the mood entry. Returns the created mood entry in a JSON response with a 201 Created status code.
   - **Request Body:**
     - JSON with the following required fields:
       - `mood` (string): The mood for the entry.
       - `mood_intensity` (integer): The intensity of the mood.
       - `note` (string): Additional details or comments about the mood.
   - **Expected Responses:**
     - **Success (201 Created):**
       - Status Code: 201
       - Body: JSON with the created mood entry.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating a validation error and the specific error messages.

![create_mood_entry_endpoint](/docs/mood_create_success.png)
![create_mood_entry_endpoint](/docs/mood_entry_bad.png)
---

## 2. Get All Mood Entries

   - **Endpoint:**
     - **URL:** `/mood_entries`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves all mood entries created by the authenticated user. Requires a valid JWT token for authentication. Returns a JSON array containing information about each mood entry.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON array with information about each mood entry.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with a message indicating missing or invalid JWT token.

![get_all_mood_entry](/docs/mood_entry_get_all.png)
![get_all_mood_entry](/docs/mood_entry_not_auth.png)
---

## 3. Get Specific Mood Entry

   - **Endpoint:**
     - **URL:** `/mood_entries/{mood_entry_id}`
     - **Method:** GET
   - **Description:** Retrieves information about a specific mood entry. Returns a JSON object with details of the mood entry. If the specified mood entry does not exist, a 404 Not Found error is returned.
   - **Parameters:**
     - `{mood_entry_id}` (int): ID of the mood entry to retrieve.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with information about the specified mood entry.
     - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating You do not have permission to access this reDocumentation.

![specific_mood_entry](/docs/specific_mood_entry.png)
![specific_mood_entry](/docs/specific_mood_no_auth.png)
---

## 4. Update Mood Entry

   - **Endpoint:**
     - **URL:** `/mood_entries/{mood_entry_id}`
     - **Method:** PUT
     - **Auth:** JWT Token (Required)
   - **Description:** Updates a specific mood entry. Only the user who created the mood entry can update it. Requires a valid JWT token for authentication. Returns the updated mood entry in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{mood_entry_id}` (int): ID of the mood entry to update.
   - **Request Body:**
     - JSON with the following optional fields:
       - `mood` (string): New mood for the entry.
       - `mood_intensity` (integer): New intensity of the mood.
       - `note` (string): New details or comments about the mood.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with the updated mood entry.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating the specific error.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with an error message indicating You do not have permission to update this reDocumentation.

![mood_entry_update](/docs/mood_entry_update_success.png)
![mood_entry_update](/docs/mood_entry_update_400.png)
![mood_entry_update](/docs/Mood_entry_update_unauth.png)
---


## 5. Delete Mood Entry

   - **Endpoint:**
     - **URL:** `/mood_entries/{mood_entry_id}`
     - **Method:** DELETE
     - **Auth:** JWT Token (Required)
   - **Description:** Deletes a specific mood entry. Only the user who created the mood entry can delete it. Requires a valid JWT token for authentication. Returns a success message in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{mood_entry_id}` (int): ID of the mood entry to delete.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified mood entry was not found.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with an error message indicating You do not have permission to delete this reDocumentation.

![delete_mood_entry](/docs/delete_mood_entry_200.png)
![delete_mood_entry](/docs/delete_mood_entry_404.png)
![delete_mood_entry](/docs/delete_mood_entry_401.png)
---

## 6. Get Depression Warning

   - **Endpoint:**
     - **URL:** `/depression_warning`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves a depression warning based on the user's average mood intensity over the last week. Requires a valid JWT token for authentication. Returns a message indicating whether a depression warning is necessary.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a depression warning message, a message indicating that no warning is necessary or not enough data.

![depression_warning](/docs/depression_warning.png)
![depression_warning](/docs/depression_warning_not_applicable.png)
![depression_warning](/docs/depression_warning_no%20data.png)
---

### Thought Journal Endpoints

## 1. Create Thought Journal Entry

   - **Endpoint:**
     - **URL:** `/thought_journals`
     - **Method:** POST
     - **Auth:** JWT Token (Required)
   - **Description:** Creates a new thought journal entry for the authenticated user. Requires a valid JWT token for authentication. The request body should contain the entry text. Returns the created thought journal entry in a JSON response with a 201 Created status code.
   - **Request Body:**
     - JSON with the following required fields:
       - `entry` (string): The text of the thought journal entry.
   - **Expected Responses:**
     - **Success (201 Created):**
       - Status Code: 201
       - Body: JSON with the created thought journal entry.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating that the entry cannot be empty.

![thought_journal_create](/docs/thought_journal_201.png)
![thought_journal_create](/docs/thought_journal_empty.png)
---

## 2. Get All Thought Journals

   - **Endpoint:**
     - **URL:** `/thought_journals`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves all thought journal entries created by the authenticated user. Requires a valid JWT token for authentication. Returns a JSON array containing information about each thought journal entry.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON array with information about each thought journal entry.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with a message indicating that no thought journals were found for this user.

![thought_journal_get](/docs/thought_journal_get.png)
![thought_journal_get](/docs/thought_journal_404.png)
---

## 3. Update Thought Journal

   - **Endpoint:**
     - **URL:** `/thought_journals/{id}`
     - **Method:** PUT
     - **Auth:** JWT Token (Required)
   - **Description:** Updates a specific thought journal entry. Only the user who created the thought journal can update it. Requires a valid JWT token for authentication. Returns the updated thought journal in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{id}` (int): ID of the thought journal entry to update.
   - **Request Body:**
     - JSON with the following required fields:
       - `entry` (string): New content for the thought journal entry.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with the updated thought journal entry.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating the specific error.
     - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating You do not have permission to update this reDocumentation.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified thought journal entry was not found.

![thought_journal_update](/docs/thought_journal_update200.png)
![thought_journal_update](/docs/thought_journal_update_400.png)
![thought_journal_update](/docs/thought_journal_update403.png)
![thought_journal_update](/docs/thought_journal_update404.png)
---

## 4. Delete Thought Journal

   - **Endpoint:**
     - **URL:** `/thought_journals/{id}`
     - **Method:** DELETE
     - **Auth:** JWT Token (Required)
   - **Description:** Deletes a specific thought journal entry. Only the user who created the thought journal can delete it. Requires a valid JWT token for authentication. Returns a success message in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{id}` (int): ID of the thought journal entry to delete.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
     - **Forbidden (403):**
       - Status Code: 403
       - Body: JSON with an error message indicating You do not have permission to delete this reDocumentation.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified thought journal entry was not found.

![thought_journal_delete](/docs/thought_journal_delete200.png)
![thought_journal_delete](/docs/thought_journal_delete403.png)
![thought_journal_delete](/docs/thought_journal_delete404.png)
---

### Goals Endpoints

## 1. Create Goal

   - **Endpoint:**
     - **URL:** `/goals`
     - **Method:** POST
     - **Auth:** JWT Token (Required)
   - **Description:** Creates a new goal for the authenticated user. Requires a valid JWT token for authentication. The request body should contain information about the goal, including the goal title, description, and an optional deadline. Returns the created goal in a JSON response with a 201 Created status code.
   - **Request Body:**
     - JSON with the following fields:
       - `goal` (string): Title or name of the goal.
       - `description` (string): Description or details of the goal (required).
       - `deadline` (string): Deadline for the goal (optional).
   - **Expected Responses:**
     - **Success (201 Created):**
       - Status Code: 201
       - Body: JSON with the created goal.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating a validation error and the specific error messages.

![goal_create](/docs/goal_create_201.png)
![goal_create](/docs/goal_create_400.png)
---

## 2. Get All Goals

   - **Endpoint:**
     - **URL:** `/goals`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves all goals belonging to the authenticated user. Requires a valid JWT token for authentication. Returns a JSON array containing information about each goal.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON array with information about each goal.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with an error message indicating missing or invalid JWT token.

![goal_get_all](/docs/goal_get_200.png)
![goal_get_all](/docs/goal_get_401.png)
---

## 3. Update Goal

   - **Endpoint:**
     - **URL:** `/goals/{goal_id}`
     - **Method:** PUT
     - **Auth:** JWT Token (Required)
   - **Description:** Updates a specific goal. Only the user who created the goal can update it. Requires a valid JWT token for authentication. Returns the updated goal in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{goal_id}` (int): ID of the goal to update.
   - **Request Body:**
     - JSON with the following optional fields:
       - `description` (string): New description for the goal.
       - `deadline` (string): New deadline for the goal.
       - `status` (string): New status for the goal.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with the updated goal.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating the specific error.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with an error message indicating You do not have permission to update this reDocumentation.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified goal was not found.

![goal_update](/docs/goal_update_200.png)
![goal_update](/docs/goal_update_400.png)
![goal_update](/docs/goal_update_401.png)
![goal_update](/docs/goal_update_404.png)
---

## 4. Delete Goal

   - **Endpoint:**
     - **URL:** `/goals/{goal_id}`
     - **Method:** DELETE
     - **Auth:** JWT Token (Required)
   - **Description:** Deletes a specific goal. Only the user who created the goal can delete it. Requires a valid JWT token for authentication. Returns a success message in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{goal_id}` (int): ID of the goal to delete.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
     - **Unauthorized (401):**
       - Status Code: 401
       - Body: JSON with an error message indicating You do not have permission to delete this reDocumentation.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified goal was not found.

![goal_delete](/docs/goal_delete_200.png)
![goal_delete](/docs/goal_delete_401.png)
![goal_delete](/docs/goal_delete_404.png)
---

### Activity Log Endpoints

## 1. Create Activity Log

   - **Endpoint:**
     - **URL:** `/activity_logs`
     - **Method:** POST
     - **Auth:** JWT Token (Required)
   - **Description:** Creates a new activity log for the authenticated user. Requires a valid JWT token for authentication. The request body should contain information about the activity log, specifically the `activity` field. Returns the created activity log in a JSON response with a 201 Created status code.
   - **Request Body:**
     - JSON with the following required field:
       - `activity` (string): The activity for the log entry.
   - **Expected Responses:**
     - **Success (201 Created):**
       - Status Code: 201
       - Body: JSON with the created activity log.
     - **Bad Request (400):**
       - Status Code: 400
       - Body: JSON with an error message indicating the specific error.

![activity_log_create](/docs/activitylog_201.png)
![activity_log_create](/docs/activitylog_400.png)
---

## 2. Get All Activity Logs

   - **Endpoint:**
     - **URL:** `/activity_logs`
     - **Method:** GET
     - **Auth:** JWT Token (Required)
   - **Description:** Retrieves all activity logs for the authenticated user. Requires a valid JWT token for authentication. Returns a JSON array containing information about each activity log.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON array with information about each activity log.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with a message indicating that no activity logs were found for the user.

![activity_log_get](/docs/activity_log_get200.png)
![activity_log_get](/docs/activity_log_get404.png)
---

## 3. Update Activity Log

   - **Endpoint:**
     - **URL:** `/activity_logs/{log_id}`
     - **Method:** PUT
     - **Auth:** JWT Token (Required)
   - **Description:** Updates a specific activity log for the authenticated user. Requires a valid JWT token for authentication. Returns the updated activity log in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{log_id}` (int): ID of the activity log to update.
   - **Request Body:**
     - JSON with the following optional fields:
       - `activity_id` (int): New activity ID for the log.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with the updated activity log.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified activity log was not found.

![activity_log_update](/docs/activity_log_update200.png)
![activity_log_update](/docs/activity_log_update404.png)
---

## 4. Delete Activity Log

   - **Endpoint:**
     - **URL:** `/activity_logs/{log_id}`
     - **Method:** DELETE
     - **Auth:** JWT Token (Required)
   - **Description:** Deletes a specific activity log for the authenticated user. Requires a valid JWT token for authentication. Returns a success message in a JSON response with a 200 OK status code.
   - **Parameters:**
     - `{log_id}` (int): ID of the activity log to delete.
   - **Expected Responses:**
     - **Success (200 OK):**
       - Status Code: 200
       - Body: JSON with a success message.
     - **Not Found (404):**
       - Status Code: 404
       - Body: JSON with an error message indicating that the specified activity log was not found.

![activity_log_delete](/docs/activity_log_delete200.png)
![activity_log_delete](/docs/activity_log_delete404.png)
---

### R6 - An ERD for your app

![moodnest_erd](/docs/MoodNest_ERD.png)
---

### R7 - Detail any third party services that your app will use


1. **Flask:**
    - *Description:* Flask stands as a lightweight and versatile web framework meticulously crafted for the purpose of constructing APIs. With its simplicity and flexibility, Flask empowers developers to define and manage URL routes, handle HTTP requests, and seamlessly integrate various extensions for enhanced functionality.
    - *Documentation:* [Flask Documentation](https://flask.palletsprojects.com/)

2. **Flask-Bcrypt:**
    - *Description:* Flask-Bcrypt plays a pivotal role in bolstering the security of your application by providing a robust mechanism for password hashing. This extension seamlessly integrates with Flask, ensuring the encryption and storage of user passwords in a secure manner.
    - *Documentation:* [Flask-Bcrypt GitHub](https://github.com/maxcountryman/flask-bcrypt)

3. **Flask-JWT-Extended:**
    - *Description:* Flask-JWT-Extended takes charge of managing JSON Web Tokens (JWTs) within your API, offering a comprehensive suite of functionalities for user authentication and authorization. Its capabilities span token creation, storage, validation, and overall JWT management.
    - *Documentation:* [Flask-JWT-Extended Documentation](https://flask-jwt-extended.readthedocs.io/)

4. **Flask-Login:**
    - *Description:* Flask-Login serves as a fundamental component for implementing user session management in your Flask application. This extension facilitates user authentication, providing a seamless and secure approach to managing user sessions.
    - *Documentation:* [Flask-Login GitHub](https://github.com/maxcountryman/flask-login)

5. **flask-marshmallow:**
    - *Description:* Flask-Marshmallow emerges as a versatile and framework-agnostic library, functioning as an Object-Relational Mapper (ORM) and Object-Document Mapper (ODM). It excels in converting complex data types, such as objects, to and from Python dictionaries, ensuring smooth data interaction in your application.
    - *Documentation:* [Flask-Marshmallow GitHub](https://github.com/marshmallow-code/flask-marshmallow)

6. **Flask-SQLAlchemy:**
    - *Description:* Flask-SQLAlchemy seamlessly integrates the power of SQLAlchemy into your Flask application, offering an elegant and intuitive approach to database interactions. By associating database tables with Python classes, Flask-SQLAlchemy simplifies the execution of database queries and manipulations.
    - *Documentation:* [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

7. **psycopg2:**
    - *Description:* Psycopg2 emerges as a crucial Python adapter facilitating seamless communication between your Python program and PostgreSQL databases. It empowers your application to interact with PostgreSQL, a robust and open-source database management system.
    - *Documentation:* [Psycopg2 Documentation](https://www.psycopg.org/docs/)

8. **marshmallow:**
    - *Description:* Marshmallow serves as a versatile Python library designed for simple yet powerful object serialization. With capabilities for data validation, formatting, and object nesting, Marshmallow enhances data management in your application, particularly when handling complex data formats like JSON.
    - *Documentation:* [Marshmallow Documentation](https://marshmallow.readthedocs.io/)

9. **marshmallow-sqlalchemy:**
    - *Description:* Marshmallow-SQLAlchemy seamlessly integrates SQLAlchemy support into your Marshmallow schemas. This integration streamlines the process of data serialization and validation, providing an effective solution for managing complex data structures in your application.
    - *Documentation:* [Marshmallow-SQLAlchemy GitHub](https://github.com/marshmallow-code/marshmallow-sqlalchemy)

10. **SQLAlchemy:**
    - *Description:* SQLAlchemy, a powerful Python SQL toolkit and Object-Relational Mapping (ORM) library, simplifies complex database interactions in your project. By allowing developers to work with Python classes instead of raw SQL queries, SQLAlchemy enhances the efficiency and maintainability of database-related code.
    - *Documentation:* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

## R8 - Describe your projects models in terms of the relationships they have with each other

### User Model

The `User` model is central to the system, representing individual users and establishing various relationships with other models. Here's an overview of key attributes and relationships:

- **id:** Primary key column uniquely identifying each user.
- **name:** Column storing the name of the user. Defaults to 'Anonymous' if not provided.
- **email:** Column storing the user's email, must be unique and not nullable.
- **password:** Column storing the user's password, must not be nullable.
- **registration_date:** Column capturing the user's registration date, defaults to the current date.
- **is_admin:** Column indicating the user's admin status, defaults to `False`.

**Relationships:**

- **mood_entries:** One-to-many relationship with the `MoodEntry` model, allowing users to have multiple associated mood entries.
- **goals:** One-to-many relationship with the `Goal` model, enabling users to have multiple associated goals.
- **activity_logs:** One-to-many relationship with the `ActivityLog` model, allowing users to have multiple associated activity logs.
- **thought_journals:** One-to-many relationship with the `ThoughtJournal` model, enabling users to have multiple associated thought journals.

The bidirectional relationships specified by `db.relationship` and `back_populates` facilitate seamless navigation between models, ensuring efficient data retrieval and management.


![User_Model](/docs/user_model.png)
---

### ThoughtJournal Model

The `ThoughtJournal` model represents a user's thoughts and entries in the system. It is intricately connected to the `User` model through a foreign key relationship. Below are the key attributes and relationships defined in the `ThoughtJournal` model:

- **id:** Primary key column uniquely identifying each thought journal entry.
- **user_id:** Foreign key column referencing the `users` table, establishing a many-to-one relationship with the `User` model.
- **entry:** Column storing the actual content of the thought journal entry. It is a text field and is marked as non-nullable, ensuring the presence of meaningful content.
- **timestamp:** Column capturing the date and time of the journal entry. It defaults to the current time and is non-nullable.

Moreover, the `ThoughtJournal` model has a bidirectional relationship with the `User` model. The `user` attribute allows easy navigation from a thought journal entry back to the associated user, and this relationship is defined using the `db.relationship` function, with `back_populates` indicating the corresponding attribute in the `User` model (`thought_journals`).

This relationship ensures that each thought journal entry is linked to a specific user, enabling efficient retrieval and management of thought journal data within the broader context of user interactions.

![Thought_journal_model](/docs/thought_journal_model.png)
---

### MoodEntry Model

The `MoodEntry` model captures information about a user's mood at a specific moment. It is closely linked to the `User` model through a foreign key relationship. Here are the key attributes and relationships defined in the `MoodEntry` model:

- **id:** Primary key column uniquely identifying each mood entry.
- **user_id:** Foreign key column referencing the `users` table, establishing a many-to-one relationship with the `User` model.
- **mood:** Column storing the mood, cannot be null.
- **mood_intensity:** Column for the intensity of the mood, cannot be null.
- **note:** Column for additional notes about the mood entry, which can be null.
- **timestamp:** Column capturing the date and time of the mood entry. Defaults to the current time and cannot be null.

Moreover, the `MoodEntry` model has a bidirectional relationship with the `User` model. The `user` attribute allows easy navigation from a mood entry back to the associated user, and this relationship is defined using the `db.relationship` function, with `back_populates` indicating the corresponding attribute in the `User` model (`mood_entries`).

This relationship ensures that each mood entry is associated with a specific user, facilitating efficient retrieval and management of mood-related data within the broader context of user interactions.

![mood_entry_model](/docs/Mood_Entry_model.png)
---

### Goal Model

The `Goal` model represents user-defined goals within the system. It maintains a connection with the `User` model through a foreign key relationship. Here are the key attributes and relationships defined in the `Goal` model:

- **id:** Primary key column uniquely identifying each goal.
- **user_id:** Foreign key column referencing the `users` table, establishing a many-to-one relationship with the `User` model.
- **goal:** Column for the goal description, cannot be null.
- **description:** Column for additional details or a description of the goal, cannot be null.
- **deadline:** Column for the deadline of the goal, which can be null.
- **status:** Column indicating the status of the goal, with a default value of "Pending" and cannot be null.
- **created_at:** Timestamp column capturing the date and time when the goal was created. Defaults to the current time and cannot be null.

Moreover, the `Goal` model has a bidirectional relationship with the `User` model. The `user` attribute allows easy navigation from a goal back to the associated user, and this relationship is defined using the `db.relationship` function, with `back_populates` indicating the corresponding attribute in the `User` model (`goals`).

This relationship ensures that each goal is associated with a specific user, enabling efficient retrieval and management of goal-related data within the broader context of user interactions.

![goal_model](/docs/goal_model.png)
---

### ActivityLog Model

The `ActivityLog` model records user activities within the system. It establishes a connection with the `User` model through a foreign key relationship. Below are the key attributes and relationships defined in the `ActivityLog` model:

- **id:** Primary key column with auto-increment, uniquely identifying each activity log entry.
- **user_id:** Foreign key column referencing the `users` table, establishing a many-to-one relationship with the `User` model.
- **activity:** Column for the recorded activity, cannot be null.
- **timestamp:** Timestamp column capturing the date and time of the activity log entry. Defaults to the current time and can be null.

Moreover, the `ActivityLog` model has a bidirectional relationship with the `User` model. The `user` attribute allows easy navigation from an activity log entry back to the associated user, and this relationship is defined using the `db.relationship` function, with `back_populates` indicating the corresponding attribute in the `User` model (`activity_logs`).

This relationship ensures that each activity log entry is linked to a specific user, facilitating the retrieval and analysis of user activities within the broader system.

![activity_log_model](/docs/Activity_log_model.png)
---

### R9 - Discuss the database relations to be implemented in your application


In my application *Moodnest*, I have defined several database relationships to effectively organize and manage data. The primary relationships are established through foreign keys and involve the following models:

### 1. User Model
- The central model representing users in the system.
- **Relationships:**
  - **Mood Entries (`mood_entries`):** One-to-many relationship allowing a user to have multiple mood entries.
  - **Goals (`goals`):** One-to-many relationship enabling a user to set and track multiple goals.
  - **Activity Logs (`activity_logs`):** One-to-many relationship recording various user activities.
  - **Thought Journals (`thought_journals`):** One-to-many relationship allowing users to maintain multiple thought journal entries.

### 2. MoodEntry Model
- Records mood-related entries for each user.
- **Relationships:**
  - **User (`user`):** Many-to-one relationship connecting each mood entry to a specific user.

### 3. Goal Model
- Represents goals set by users.
- **Relationships:**
  - **User (`user`):** Many-to-one relationship linking each goal to a specific user.

### 4. ThoughtJournal Model
- Stores entries related to user's thoughts.
- **Relationships:**
  - **User (`user`):** Many-to-one relationship associating each thought journal entry with a specific user.

### 5. ActivityLog Model
- Records various activities of users within the system.
- **Relationships:**
  - **User (`user`):** Many-to-one relationship connecting each activity log entry to a specific user.

These relationships are defined to ensure data consistency, integrity, and efficient retrieval. They allow the application to organize information in a structured manner, reflecting the real-world connections between users, their moods, goals, thoughts, and activities. Additionally, the use of cascading options in some relationships ensures that related records are appropriately handled when a user or associated entity is modified or deleted.

---

### R10 - Describe the way tasks are allocated and tracked in your project

For my API webserver project, *Moodnest*, I opted to utilise the program 'Linear' to structure and manage various phase issues. I organised these issues into a backlog, to-do, in-progress, and done, facilitating the completion of "sprints" and advancing through specific project phases on a daily basis. Planning this framework at the project's outset proved highly advantageous, ensuring efficiency throughout the development process. Screenshots from Linear show my progression through these tasks.

Additionally, I actively participated in daily stand up meetings on the Coder Academy Discord platform. These sessions held me accountable each day, allowing me to report on my accomplishments in the previous 24 hours, address any challenges or blockers hindering project completion, outline my approach for the next 24 hours, and share new insights gained that day. This practice proved exceptionally beneficial, providing insights into the progress of fellow students.

I also maintained a consistent practice of making regular commits to GitHub. This contributed to a clear and traceable development path, offering a record of the project's evolution and showcasing the milestones achieved thus far.

Please see images below.

