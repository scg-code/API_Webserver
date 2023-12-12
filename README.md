# SamuelGifford_T2A2 - API Web Server

![MoodNest](/docs/Moodnest.png)

### R0 - Introduction

*MoodNest* is a comprehensive and user-centric mental health check-in platform designed to address the growing need for accessible tools for daily mental well-being management. With a focus on proactive mental health, *MoodNest* aims to empower individuals to reflect on their mental well-being, track their emotions, and develop strategies for self-care. By providing a stigma-free environment and fostering a culture of openness, *MoodNest* strives to contribute to a healthier and more resilient society that prioritizes mental well-being.

---

## Table of Contents
- [R1 - Identification of the problem you are trying to solve by building this particular app](#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)
- [R2 - Why is it a problem that needs solving?](#r2---why-is-it-a-problem-that-needs-solving)
- [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
- [R4 - Identify and discuss the key functionalities and benefits of an ORM](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)

---

### R1 - Identification of the problem you are trying to solve by building this particular app.
In the contemporary landscape, mental health has emerged as a critical facet of overall well-being, with an increasing global awareness of the huge impact of mental health challenges on individuals and societies. The problem at hand revolves around the substantial gap between the prevalence of mental health concerns and the accessibility of effective tools for daily mental well-being check-ins and management.  *MoodNest* endeavours to address this multifaceted challenge by providing a comprehensive and user-centric mental health check-in platform.

Global statistics underscore the gravity of mental health challenges. According to the World Health Organization (WHO), over 450 million people worldwide suffer from mental health disorders! Making mental health conditions a leading cause of ill-health and disability globally. Despite the staggering prevalence, a massive proportion of individuals do not have easy access to personalised and supportive platforms for regular mental health check-ins. 

A critical aspect of the problem lies in the underutilization of available mental health services. According to the Australian Institute of Health and Welfare (AIHW), nearly 65% of Australians with mental health disorders did not access mental health services in 2020. Stigma, lack of awareness, and societal attitudes continue to hinder individuals from seeking necessary support. *MoodNest* endeavours to challenge this underutilization by providing an Australian-centric, stigma-free environment that encourages individuals to engage in daily reflections on their mental well-being.

The workplace is a significant arena for mental health challenges in Australia as well. Work-related stress has been identified as a prominent issue affecting productivity. A study by *BeyondBlue*, an Australian mental health organization, reveals that work-related stress costs the Australian economy over $10 billion per year. The demanding nature of work environments, exacerbated by factors such as remote work and job uncertainty, underscores the need for targeted strategies. *MoodNest* acknowledges the impact of workplace stress on mental health and productivity, positioning itself as a valuable resource for Australians seeking daily strategies to manage stress and achieve a healthier work-life balance.

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

8. **Strategic Resource Allocation:**
   - By addressing mental health concerns through *MoodNest*, there is an opportunity to strategically allocate resources. Proactive mental health management can potentially alleviate the burden on traditional healthcare services, allowing for more efficient resource utilization and a more equitable distribution of mental health support.

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

6. **Open-Source Nature:** PostgreSQL being truly open-source and community-driven ensures transparency, community support, and continuous improvement. It aligns with the project's commitment to open-source principles.

### Drawbacks Compared to Others, Such as MySQL:

1. **Popularity and Ecosystem:** PostgreSQL is less popular than MySQL, resulting in a smaller ecosystem of third-party tools and a potentially smaller pool of available developers and administrators. This might impact the availability of resources and community support.

2. **Resource Consumption:** PostgreSQL forks a new process for each client connection, allocating a non-trivial amount of memory (about 10 MB per process). This can lead to higher resource consumption compared to databases like MySQL, which may impact scalability in certain scenarios.

3. **Read-Heavy Workloads:** For simple, read-heavy workflows, where speed is a higher priority than some advanced features, PostgreSQL might be perceived as a less optimal choice compared to MySQL. MySQL has historically excelled in read-heavy scenarios.

4. **Familiarity and Comfort:** The choice of PostgreSQL may pose a challenge in environments where MySQL is more familiar and comfortable for developers. Overcoming the learning curve associated with a less familiar database system could be considered a drawback.

In conclusion, while PostgreSQL was selected for its advanced features, strong concurrency handling, and adherence to SQL standards, it's essential to acknowledge potential drawbacks, including ecosystem considerations, resource consumption, and challenges in environments where MySQL is more prevalent. The decision to prioritize advanced features and data integrity influenced the selection, accepting trade-offs in areas where PostgreSQL might be perceived as less advantageous.


Sources:

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


#### User Endpoints

1. Register
    - Endpoint
       - URL: /register
       - Method: POST
       - Auth: None Required
       - Description: The /register endpoint allows users to sign up by providing registration information. No authentication is required, and successful registration results in the creation of a new user account. If the provided email is already in use, a conflict error is returned.
       - Expected Responses: 
         - Status Code: 201 (Created)
         - Body: JSON containing the user's name, email and a success message.
         - Status Code: 409 (Conflict)
         - Body: JSON with an error message indicating that the provided email is already in use.


![Register_endpoint](/docs/Register_User.png)
![Register_endpoint](/docs/Email_in_use.png)
---


2. Login
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

3. Get ALL users
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

4. Delete User
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

5. Get User Stats
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

6. Change User Details
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

1. Create Mood Entry

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

2. Get All Mood Entries

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

3. Get Specific Mood Entry

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
       - Body: JSON with an error message indicating You do not have permission to access this resource.

![specific_mood_entry](/docs/specific_mood_entry.png)
![specific_mood_entry](/docs/specific_mood_no_auth.png)
---

4. Update Mood Entry

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
       - Body: JSON with an error message indicating You do not have permission to update this resource.

![mood_entry_update](/docs/mood_entry_update_success.png)
![mood_entry_update](/docs/mood_entry_update_400.png)
![mood_entry_update](/docs/Mood_entry_update_unauth.png)
---


5. Delete Mood Entry

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
       - Body: JSON with an error message indicating You do not have permission to delete this resource.

![delete_mood_entry](/docs/delete_mood_entry_200.png)
![delete_mood_entry](/docs/delete_mood_entry_404.png)
![delete_mood_entry](/docs/delete_mood_entry_401.png)
---

6. Get Depression Warning

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



### R6 - An ERD for your app


### R7 - Detail any third party services that your app will use


### R8 - Describe your projects models in terms of the relationships they have with each other


### R9 - Discuss the database relations to be implemented in your application


### R10 - Describe the way tasks are allocated and tracked in your project# API_Webserver
