import React from 'react';
import { Link } from 'react-router-dom';
import { Carousel } from "react-bootstrap";
import ab from './about.jpg'; // Background image
// import ab from '../about.jpg';

const Home = () => {
    return (
        <>
            {/* Start Background image */}
            <section className="showcase" style={{
                backgroundImage: `url(${ab})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
                backgroundRepeat: 'no-repeat',
                minHeight: '70vh', // Adjust the height here
                display: 'flex',
                alignItems: 'center', // Vertically center content
            }}>
                <div className="overlay"></div>
                <div className="text">
                    <h1 className='head'>Never stop learning.<br /> Never stop growing.</h1>
                    <h1 className='headss'>Learn with Us!</h1>
                    <p className='para'>Learn from the top Instructors over the World.<br />Learn the latest Technology Trends.</p>
                </div>
            </section>
            {/*  End Background image */}
            {/*  Start Features of meetLearning*/}
            <div className="container py-5">
                <div className="row">
                    {/* Features go here */}
                </div>
            </div>
            {/*  End Features of meetLearning*/}
        </>
    )
}

export default Home;
