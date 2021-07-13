Django Framework Project
"Textile Market" - application for publishung a textile manufacturing offers in order to be achieved best price and terms.

The application:
-is implemented using Django Framework.
-14 endpoints.
-login/register functionality.
-public part (A part of the website, which is accessible by everyone – un/authenticated users and admins)
-private part (accessible only by authenticated user and admins) where permissitions depends of user's group ("User" or "Company")
-admin part (accessible only to admins)
-unauthenticated users (public part) have only 'get' permissions e.g., home page, a brief overview of the published offers 
-authenticated users of group "User" (private part) have detailed overview of the published offers and full CRUD for their created profile
-authenticated users of group "Company" (private part) have full CRUD for their created profile and published offers.
-admins have full CRUD functionalities
-Error Handling and Data Validations
-PostgreSQL as a database
-file storage cloud Cloudinary for storing the files
-tests on business logic
-template inheritance
-source control system Github or Gitlab
-class-based views (ListView)
-extended Django user

