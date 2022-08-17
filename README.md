# Sell Your Bike
## Installation Guide:
**Dependencies**
1. Python 3.X
2. Flask

**Clone the repository:**

`git clone https://github.com/Anshikasoni/TCS-iON`

**Install required libraries**

Run this from a terminal in the project directory: 

` pip install -r requirements `

**Run the application**
Run this from a terminal in the project directory:

` python app.py `

## Website guide:

### Home Page

Open the URL and you can see this screen: 

![image](https://user-images.githubusercontent.com/44340358/185262013-0e854ff1-2e21-4a9c-863c-66e8644159de.png)

For first time users, you'd have to register yourself.

**Click on Register Now!! button**

Enter your details:

![image](https://user-images.githubusercontent.com/44340358/185262178-cac3a683-7afc-4616-ae4a-5e6a727ee1e5.png)

Click on Submit.

**Now your details are being saved in Database (users table) and you can now login using the details you provided during registration**

### Login
Click on "Login" from homepage:

![image](https://user-images.githubusercontent.com/44340358/185262482-bfe81253-e7c0-4549-b9e4-0ef25cc610c1.png)

Feed your details on the login page:

![image](https://user-images.githubusercontent.com/44340358/185262561-39b755fd-9b43-43f4-a126-9d6952b9530e.png)

Then press Submit and you will be redirected to home page

By default, the users created are of customer role only, but we have two screens:
1. Admin: Here you can see the responses collected from contact us form:

  ![image](https://user-images.githubusercontent.com/44340358/185262692-ab8cf2fd-4bba-48ae-a7cc-e27889472417.png)

2. Customers: The screen is normal, just we can't see the responses from here:

  ![image](https://user-images.githubusercontent.com/44340358/185262855-9a7f0d3f-f61d-45b5-bf6b-038d7e76c795.png)

### Contact Us
To access this page, click on "Contact Us" on the navbar of any page:

![image](https://user-images.githubusercontent.com/44340358/185262980-8f3f460d-a7b8-45f1-8de8-5821593c7315.png)

You will be presented with a form, asking for basic details.
Post entering the details, click on Submit

The details will then be saved to the database (contactus table)
Which then can be viewed from Admin user home page.
