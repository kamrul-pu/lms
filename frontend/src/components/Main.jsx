import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './Header/Header';
import Footer from './Footer/Footer';
import Home from './Body/Home';
import UserLogout from './UserLogout';
import Login from './Login';

const Main = () => {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/user-logout' element={<UserLogout />} />
                <Route path='/user-login' element={<Login />} />
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default Main