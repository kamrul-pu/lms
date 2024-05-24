import React from 'react'
import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom';
import { useEffect } from 'react'
import { useState } from 'react'
import Swal from 'sweetalert2'
import axios from 'axios'

const baseUrl = 'http://localhost:8000/api/v1/courses/all?category=';

const CategoryCourses = () => {
  const access_token = localStorage.getItem("access_token");
  useEffect(() => {
    document.title = 'LMS | Our Categories'
  })

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

  const [courseData, setCourseData] = useState([]);
  const { category_slug } = useParams();
  const [nextUrl, setNextUrl] = useState();
  const [previousUrl, setPreviousUrl] = useState();

  useEffect(() => {
    fetchData(baseUrl + category_slug)
  }, []);

  const paginationHandler = (url) => {
    fetchData(url)
  }

  function fetchData(url) {
    try {
      axios.get(url, {
        headers: {
          Authorization: `Bearer ${access_token}`
        }
      })
        .then((res) => {
          setNextUrl(res.data.next)
          setPreviousUrl(res.data.previous)
          setCourseData(res.data.results)
        });
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [])

  return (
    <div className='container mt-4'>
      <h3 className=' pb-1 mb-4 mt-5'>{category_slug}</h3>
      <div className='row mb-4'>
        {courseData && courseData.map((course, index) =>
          <div className='col-md-3 mb-3'>
            <div className="card">
              <Link to={`/detail/${course.id}`}><img src={course.image} height={200} className="card-img-top" alt={course.name} /></Link>
              <div className="card-body">
                <h5 className="card-title"><Link to={`/detail/${course.slug}`}>{course.name}</Link></h5>
              </div>
            </div>
          </div>
        )}
      </div>
      <nav aria-label="Page navigation example mt-3">
        <ul className="pagination justify-content-center">
          {previousUrl &&
            <li className='page-item'><button className='page-link' onClick={() => paginationHandler(previousUrl)}><i className='bi bi-arrow-left'></i>Previous</button></li>
          }
          {nextUrl &&
            <li className='page-item'><button className='page-link' onClick={() => paginationHandler(nextUrl)}><i className='bi bi-arrow-right'></i>Next</button></li>
          }
        </ul>
      </nav>
    </div>
  )
}

export default CategoryCourses
