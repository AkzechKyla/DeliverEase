# DeliverEase

DeliverEase is a prototype routing system designed to streamline route planning for delivery riders. This system optimizes delivery routes to save time, reduce fuel consumption, and enhance efficiency, making the delivery process smoother and more reliable.

![image](https://github.com/user-attachments/assets/9e7de2d0-8265-4658-99c8-b043d879788b)
![image](https://github.com/user-attachments/assets/bef2a576-09a1-4116-8ae2-d8c50200ea68)


## Features

- 3D landing page
- Google Maps views (default, satellite, terrain, and street)
- Manage list of deliveries (add, delete, optimize, and reset)
- Set source location
- Auto map panning
- Polylines for route
- Map markers for source and destination locations

# Tech Stack

## Landing Page
- React
- Vite
- Tailwind CSS
- Three.js
- Framer Motion
- React Three Fiber

## Routing System
- HTML
- CSS
- JavaScript
- Google Maps API
- Overpass API

# Test the Application
1. Visit akzechkyla.github.io/DeliverEase/
2. On the landing page, scroll down and click **View App**.
![image](https://github.com/user-attachments/assets/ba79a95c-a3e9-4755-b194-96987e2f0daa)
![image](https://github.com/user-attachments/assets/6f81d145-8884-4f0e-902a-123b0731c241)
![image](https://github.com/user-attachments/assets/adbd1b46-e719-45ec-bc7b-b20972c0ae28)
3. You'll be redirected to a map with a default starting location. You can keep it or enter a different location in the search bar. Note: The system works effectively within Manila and Quezon City; results may be inaccurate outside this area.
  ![image](https://github.com/user-attachments/assets/8bdf6f5d-33ce-4bb0-a523-3ca1e8a58264)
4. The app uses mock delivery data. Copy and paste any of the following order IDs into the app:
```
Order ID

2406069U1PVRCM
240528H1NP8TQS
24052340GFPN7G
240506K4VFWEK5
240506K4KX9F6H
240424HXYQ5GJ2
2404183QBAB6QT
240425N8AM7X09
2404196ERP2Q7T
2404086CK36S6J
2404170BXAY2CA
2404063AEH0P2Q
2404074JQM6CAN
240405VP8VDM0E
240330DB2U0UWK
2403288QRTN7F0
2403288NAUTFAX
240320J1X86MJM
2403154QC3E3VE
240306BQQ4374A
```
![image](https://github.com/user-attachments/assets/0d9b5964-8eb6-4020-b078-21af9396ecbc)

5. Click **Optimize Deliveries** button.
![image](https://github.com/user-attachments/assets/7c68d405-a9d0-4a36-b03d-1fa61d1c8979)

6. Explore the Google Maps view or click **Reset** to clear the delivery list.

# Contributors
<table border="1">
  <tr>
    <th>Name</th>
    <th>Role</th>
    <th>Contributions</th>
  </tr>
  <tr>
    <td><a href="https://github.com/akzechkyla">AkzechKyla</a></td>
    <td>Lead Developer</td>
    <td>Implemented core functionalities</td>
  </tr>
  <tr>
    <td><a href="https://github.com/feiryrej">Feiryrej</a></td>
    <td>Frontend Developer</td>
    <td>Implemented landing page and UI map design</td>
  </tr>
  <tr>
    <td><a href="https://github.com/dotBisch">DotBisch</a></td>
    <td>Server-side Developer</td>
    <td>Implemented Overpass API endpoint and prepared mock data</td>
  </tr>
</table>
