import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Swal from 'sweetalert2';

const baseUrl = 'http://localhost:8000/api/v1';

const Login = () => {
  useEffect(() => {
    document.title = 'LMS | Login';
    window.scrollTo(0, 0);
  }, []);

  const [loginData, setLoginData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (event) => {
    setLoginData({
      ...loginData,
      [event.target.name]: event.target.value
    });
  }

  const submitForm = async () => {
    try {
      const response = await axios.post(baseUrl + "/token", loginData);
      const { access, refresh } = response.data;

      // Store tokens in local storage
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      localStorage.setItem('studentLoginStatus', true);

      const user = await axios.get(baseUrl + "/users/me", {
        headers: {
          Authorization: `Bearer ${access}`
        }
      })

      localStorage.setItem("userData", user.data);

      // Redirect to dashboard
      window.location.href = '/user-dashboard';
    } catch (error) {
      console.error('Login Error:', error);
      Swal.fire({
        title: 'Invalid Credentials!',
        icon: 'error',
        toast: true,
        timer: 2000,
        position: 'top',
        timerProgressBar: true,
        showConfirmButton: false
      });
    }
  }

  return (
    <div className="container">
      <div className="row">
        <div className="col-sm-9 col-md-7 col-lg-5 mx-auto">
          <div className="card border-0 shadow rounded-3 my-5">
            <div className="card-body p-4 p-sm-5">
              <div className="text-center wow fadeInUp">
                <h5 className="card-title text-center mb-3 fw-light fs-5 text-dark">STUDENT SIGN IN</h5>
              </div>
              <div className="form-floating mb-3">
                <input type="email" value={loginData.email} onChange={handleChange} name='email' className="form-control" id="floatingInput" placeholder="name@example.com" />
                <label htmlFor="floatingInput">Email address</label>
              </div>
              <div className="form-floating mb-3">
                <input value={loginData.password} name='password' type="password" onChange={handleChange} className="form-control" id="floatingPassword" placeholder="Password" />
                <label htmlFor="floatingPassword">Password</label>
              </div>
              <div className="d-grid my-4">
                <button onClick={submitForm} className="btn btn-success rounded-pill btn-login text-uppercase fw-bold" type="button">Sign in</button>
                <hr />
                <Link to='/user-register' className="btn btn-danger rounded-pill btn-login text-uppercase fw-bold">SIGN UP</Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
