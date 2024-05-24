import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Swal from 'sweetalert2';

const baseUrl = 'http://localhost:8000/api/v1/users';

const Register = () => {
  useEffect(() => {
    document.title = 'LMS | Student Register';
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const [studentData, setStudentData] = useState({
    'first_name': '',
    'last_name': '',
    'phone': '',
    'email': '',
    'gender': '',
    'kind': 'STUDENT', // Default value is 'STUDENT'
    'image': null, // Default value is null
    'password': '',
    'confirm_password': '',
    'status': ''
  });

  const handleChange = (event) => {
    setStudentData({
      ...studentData,
      [event.target.name]: event.target.value
    });
  }

  const submitForm = () => {
    const studentFormData = new FormData();
    studentFormData.append("first_name", studentData.first_name);
    studentFormData.append("last_name", studentData.last_name);
    studentFormData.append("phone", studentData.phone);
    studentFormData.append("email", studentData.email);
    studentFormData.append("gender", studentData.gender);
    studentFormData.append("kind", studentData.kind);
    studentFormData.append("image", studentData.image); // Image field as a file
    studentFormData.append("password", studentData.password);
    studentFormData.append("confirm_password", studentData.confirm_password);

    try {
      axios.post(`${baseUrl}/register`, studentFormData)
        .then((response) => {
          setStudentData({
            'first_name': '',
            'last_name': '',
            'phone': '',
            'email': '',
            'gender': '',
            'kind': 'STUDENT',
            'image': null,
            'password': '',
            'confirm_password': '',
            'status': 'success'
          });
          if (response.status === 200 || response.status === 201) {
            Swal.fire({
              title: 'Register Successfully!',
              icon: 'success',
              toast: true,
              timer: 2000,
              position: 'top-right',
              timerProgressBar: true,
              showConfirmButton: false
            });
            // Redirect to login after successful registration
            setTimeout(() => {
              window.location.href = '/user-login';
            }, 2500);
          }
        });
    } catch (error) {
      console.log(error);
      setStudentData({ 'status': 'error' });
    }
  }

  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col-sm-9 col-md-7 col-lg-5 mx-auto">
            <div className="card border-0 shadow rounded-3 my-5">
              <div className="card-body p-4 p-sm-5">
                <div className="text-center wow fadeInUp">
                  <h5 className="card-title text-center mb-3 fw-light fs-5 text-dark ">STUDENT SIGN UP</h5>
                </div>
                {studentData.status === 'success' && <h3 className='text-center text-success mb-3'>Registered Successfully</h3>}
                {studentData.status === 'error' && <h3 className='text-center text-danger mb-3'>Something wrong has happened</h3>}
                <div className="form-floating mb-3">
                  <input type="text" onChange={handleChange} name='first_name' className="form-control" id="floatingInput" placeholder="First Name" />
                  <label htmlFor="floatingInput">First Name</label>
                </div>
                <div className="form-floating mb-3">
                  <input type="text" onChange={handleChange} name='last_name' className="form-control" id="floatingInput" placeholder="Last Name" />
                  <label htmlFor="floatingInput">Last Name</label>
                </div>
                <div className="form-floating mb-3">
                  <input type="text" onChange={handleChange} name='phone' className="form-control" id="floatingInput" placeholder="Phone" />
                  <label htmlFor="floatingInput">Phone</label>
                </div>
                <div className="form-floating mb-3">
                  <input type="email" onChange={handleChange} name='email' className="form-control" id="floatingInput" placeholder="name@example.com" />
                  <label htmlFor="floatingInput">Email Id</label>
                </div>
                <div className="form-floating mb-3">
                  <select onChange={handleChange} name='gender' className="form-select" id="floatingGender">
                    <option value="">Select Gender</option>
                    <option value="MALE">Male</option>
                    <option value="FEMALE">Female</option>
                    <option value="OTHER">Other</option>
                  </select>
                  <label htmlFor="floatingGender">Gender</label>
                </div>
                <div className="form-floating mb-3">
                  <input type="file" onChange={(e) => setStudentData({ ...studentData, image: e.target.files[0] })} name='image' className="form-control" id="floatingInput" />
                  <label htmlFor="floatingInput">Image</label>
                </div>
                <div className="form-floating mb-3">
                  <input name='password' type="password" onChange={handleChange} className="form-control" id="floatingPassword" placeholder="Password" />
                  <label htmlFor="floatingPassword">Password</label>
                </div>
                <div className="form-floating mb-3">
                  <input name='confirm_password' type="password" onChange={handleChange} className="form-control" id="floatingConfirmPassword" placeholder="Confirm Password" />
                  <label htmlFor="floatingConfirmPassword">Confirm Password</label>
                </div>
                <div className="d-grid my-4">
                  <button onClick={submitForm} className="btn btn-success rounded-pill btn-login text-uppercase fw-bold" type="submit" >SIGN UP</button>
                  <hr className='' />
                  <Link to='/user-login' className="btn btn-danger rounded-pill btn-login text-uppercase fw-bold">SIGN IN</Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Register;
