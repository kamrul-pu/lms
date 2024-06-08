import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './Header/Header';
import Footer from './Footer/Footer';
import Home from './Body/Home';
import UserLogout from './UserLogout';
import Login from './Login';
import AllCourses from './Body/AllCourses';
import Category from './Body/Category';
import CategoryCourses from './Body/CategoryCourses';
import CourseDetail from './Body/CourseDetail';

const Main = () => {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/user-logout' element={<UserLogout />} />
                <Route path='/user-login' element={<Login />} />
                <Route path='/courses' element={<AllCourses />} />
                <Route path='/category' element={<Category />} />
                <Route path='/course/category/:category_slug' element={<CategoryCourses />} />
                <Route path='courses/:course_slug' element={<CourseDetail />} />
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default Main