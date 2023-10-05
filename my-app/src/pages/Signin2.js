import React from 'react';
import './Signin2.css';
import moonpic from '../assets/moon (1) 2.png';
import logo from '../assets/Screenshot_2023-09-20_201047-removebg-preview.png';

const Signin2 = () => {
  return (
    <div>
      <div className="colourmode">
        <img src={moonpic} alt="moon" className="moon"></img>
      </div>
      <div className="signin">
        <img src={logo} alt="moon" className="logo"></img>
        <div className="heading_signin">Trustvault</div>
        <div className="subheading_signin">Sign Up</div>
        <div className="input_signin">
          <input type="text" for="input_field_username" placeholder="Password" className="password_signin2"></input>
          <br/>
          <input type="text" placeholder="Confirm" className="confirm_signin2"></input>
        </div>
        <div className="submit_button">Next &#x2192;</div>
      </div>
    </div>
  )
}

export default Signin2