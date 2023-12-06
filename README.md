# SamuelGifford_T2A2 - API Web Server - *MoodNest*

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


### R6 - An ERD for your app


### R7 - Detail any third party services that your app will use


### R8 - Describe your projects models in terms of the relationships they have with each other


### R9 - Discuss the database relations to be implemented in your application


### R10 - Describe the way tasks are allocated and tracked in your project# API_Webserver
