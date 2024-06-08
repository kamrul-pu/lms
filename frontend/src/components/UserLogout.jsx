import React from 'react'

const UserLogout = () => {
  localStorage.removeItem('studentLoginStatus');
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('userData');
  window.location.href = '/user-login';
  return (
    <div>

    </div>
  )
}

export default UserLogout;
