import React from 'react'
import './Register.css'
import moonpic from '../assets/moon (1) 2.png'
import logo from '../assets/Screenshot_2023-09-20_201047-removebg-preview.png'
import google from '../assets/Untitled design 1.png'

const Register = () => {
  return (
    <div>
      <div className="colourmode">
        <img src={moonpic} alt="moon" className="moon"></img>
      </div>
      <div className="register">
        <img src={logo} alt="moon" className="logo"></img>
        <div className="heading_register">Trustvault</div>
        <div className="subheading_register">Sign In</div>
        <div className="input_register">
          <input type="text" for="input_field_username" placeholder="Email" className="email_register"></input>
          <br/>
          <input type="text" placeholder="Password" className="password_register"></input>
        </div>
        <div className="submit_button_register">Next &#x2192;</div>
        <div className='create_account'>Create Account</div>
        <div className='google'>
            <img src={google} alt="google" className="google_logo"></img>
            <div className='sign_in_with_google'>Sign in with Google</div>
        </div>
      </div>
    </div>
  )
}

export default Register