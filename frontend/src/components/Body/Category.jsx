import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const baseUrl = 'http://localhost:8000/api/v1/courses/category';

const Category = () => {
  const [categoryData, setCategoryData] = useState([]);

  useEffect(() => {
    document.title = 'LMS | Our Categories';
    fetchCategoryData();
  }, []);

  const fetchCategoryData = async () => {
    try {
      const response = await axios.get(baseUrl);
      setCategoryData(response.data["results"]);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className='container mt-4'>
      <div className="text-center wow fadeInUp">
        <h6 className="section-title bg-white text-primary px-3">Categories</h6>
        <h1 className="mb-5">Our Categories</h1>
      </div>
      <div className='row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4'>
        {categoryData.map((row, index) => (
          <div className='col' key={index}>
            <div className="card h-100">
              {row.image && (
                <img src={row.image} className="card-img-top" alt={row.name} style={{ height: '200px', objectFit: 'cover' }} />
              )}
              <div className="card-body">
                <h5 className="card-title"><Link to={`/course/category/${row.slug}`} className="text-decoration-none text-dark">{row.name}({row.total_courses})</Link></h5>
                <p className='card-text'>{row.description}</p>
                <p className="card-text"><small className="text-muted">Total Courses: {row.total_courses}</small></p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Category;
