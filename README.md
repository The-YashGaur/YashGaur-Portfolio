# Yash Gaur - Professional Portfolio

Welcome to the repository for my personal portfolio website! This project is a modern, highly interactive, and responsive web application designed to showcase my skills, projects, and professional journey.

## 🚀 Features

- **Stunning UI/UX**: Built with modern design principles, dark mode support, and smooth scroll animations.
- **Interactive 3D Profile Card**: A dynamic, mouse-tracking 3D profile card built with CSS and Framer Motion.
- **Projects Showcase**: A dedicated section to display my latest development projects with direct links and tech tags.
- **Certifications Gallery**: An organized view of my professional certificates and achievements.
- **Real-time Contact Form**: Visitors can send messages directly to me. Data is securely stored using Supabase.
- **Public Comment/Review System**: Users can leave public comments on the portfolio, which are stored and fetched in real-time.
- **Secure Admin Dashboard**: A hidden, password-protected admin panel to view contact messages and manage user comments.

## 💻 Tech Stack

This project is built using cutting-edge web technologies:

- **Frontend Framework**: [React.js](https://reactjs.org/) with [Vite](https://vitejs.dev/) for lightning-fast builds.
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) for utility-first styling and responsive design.
- **Animations**: [Framer Motion](https://www.framer.com/motion/) for complex, smooth, and interactive animations.
- **Backend / Database**: [Supabase](https://supabase.com/) (PostgreSQL) for handling the contact form, comments, and admin authentication.
- **Icons**: [React Icons](https://react-icons.github.io/react-icons/) (FontAwesome, SimpleIcons).

## 🛠️ Local Development Setup

To run this project locally on your machine, follow these steps:

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn
- A Supabase account (for database features)

### 1. Clone the repository
```bash
git clone https://github.com/The-YashGaur/Yash-portofolio-main.git
cd Yash-portofolio-main
```

### 2. Install dependencies
```bash
npm install
```

### 3. Set up Environment Variables
Create a `.env` file in the root directory of the project and add your Supabase credentials:
```env
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 4. Set up Supabase Database
You will need to create the following tables in your Supabase SQL editor for the backend features to work:
- `contact_messages` (id, created_at, name, email, message, status)
- `comments` (id, created_at, name, message, likes)
- `admins` (admin_id, username, password, last_login)

*Note: The SQL setup scripts are available in the project documentation/artifacts.*

### 5. Run the development server
```bash
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser to view the application.

## 🚀 Deployment

This project is optimized for deployment on [Vercel](https://vercel.com).
1. Import the repository into Vercel.
2. Add your `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` to the Vercel Environment Variables.
3. Deploy!

## 📄 License

COPYRIGHT (c) 2024-2026 Yash Gaur. All rights reserved.
This project and its source code are the intellectual property of Yash Gaur. 
For detailed terms, please refer to the `LICENSE` file.

---
*Built with ❤️ by Yash Gaur*
