import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Swal from 'sweetalert2';

const CourseDetail = () => {
  const [courseData, setCourseData] = useState({});
  const [enrolledStatus, setEnrolledStatus] = useState(false);
  const [userLoginStatus, setUserLoginStatus] = useState(false);
  const { course_slug } = useParams();
  const access_token = localStorage.getItem("access_token");

  useEffect(() => {
    fetchCourseData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const fetchCourseData = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/courses/all/${course_slug}`, {
        headers: {
          Authorization: `Bearer ${access_token}`
        }
      });
      setCourseData(response.data);
      setEnrolledStatus(response.data.is_enrolled);
    } catch (error) {
      console.log(error);
    }
  };

  const enrollCourse = async () => {
    try {
      const formData = new FormData();
      console.log("course data", courseData)
      formData.append('course_id', courseData.id);
      await axios.post("http://127.0.0.1:8000/api/v1/courses/enrollments", formData, {
        headers: {
          'content-type': 'multipart/form-data',
          Authorization: `Bearer ${access_token}`
        }
      });
      Swal.fire({
        title: 'You Successfully Enrolled!',
        icon: 'success',
        toast: true,
        timer: 3000,
        position: 'top-right',
        timerProgressBar: true,
        showConfirmButton: false
      });
      setEnrolledStatus(true);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    const studentLoginStatus = localStorage.getItem('studentLoginStatus');
    if (studentLoginStatus === 'true') {
      setUserLoginStatus(true);
    }
  }, []);

  return (
    <div className='container mt-4 px-4'>
      <div className='row'>
        <div className='col-lg-3 col-md-6 mt-3'>
          <div className='team-item bg-light'>
            <div className='overflow-hidden' style={{ width: '200px', height: '200px' }}>
              <img src={courseData.image} className='card-img-top img-fluid img-thumbnail' alt={courseData.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
            </div>
          </div>
        </div>
        <div className='col-8 pd-2 mt-3'>
          <h3>{courseData.name}</h3>
          <h4>{courseData.sub_title}</h4>
          <h5>Level: {courseData.level}</h5>
          <h5>Enrolled: {enrolledStatus}</h5>
          <h5>Duration: {courseData.duration}</h5>
          <p>Price: {courseData.price} Discount: {courseData.discount_percentage}% Total: {courseData.total_price}</p>
          <hr />
          <p>{courseData.description}</p>
          {courseData.instructor && (
            <p className='fw-bold'>Course By : {courseData.instructor.first_name} {courseData.instructor.last_name}</p>
          )}
          {userLoginStatus && !enrolledStatus && (
            <p><button type='button' className='btn btn-success rounded-pill' onClick={enrollCourse}>Enroll in this Course</button></p>
          )}
          {userLoginStatus && enrolledStatus && (
            <p><span className='btn btn-info rounded-pill btn-sm'>You are already Enrolled in this Course</span></p>
          )}
        </div>
      </div>
    </div>
  );
}

export default CourseDetail;
