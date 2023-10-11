import React from "react";
import icon from "../assets/Screenshot_2023-09-20_201047-removebg-preview.png";
import "./LandingPage.css";
import metamask from "../assets/Untitled_design__9__1-removebg-preview.png";
import blockdiagram from "../assets/original-4cfe1ccf4ff167f1e18b27afe33c1f5d 1.png";
import moonpic from "../assets/moon (1) 2.png";
import { Link } from "react-router-dom";

const LandingPage = () => {
  return (
    <div className="landing">
      <div className="navbar">
        <img className="icon" alt="icon" src={icon}></img>
        <div className="heading">TrustVault</div>
        <div className="aboutbox">
        <Link to="/about" >
          <div className="about">
          About
          </div>
          </Link>
        </div> 
        <div className="colourmode">
          <img src={moonpic} alt="moon" className="moon"></img>
        </div>
        <div className="connect">
          <img src={metamask} alt="metamask" className="metamask" />
          <div className="connectbutton">
            <div className="Connect">Connect</div>
          </div>
        </div>
      </div>
      <div className="main">
        <div className="welcomecontent">
          Easy and Secure access to your Document
        </div>
        <img src={blockdiagram} alt="blockdiagram" className="blockdiagram" />
        <Link to="/description">
        <button className="learnmore">Learn More</button></Link>
        <div className="subheading">
          Services We <br />
          Provide
        </div>
        <div className="servicesweprovide">
          <div className="serviceno1">
            Secure Blockchain-Based Legal Record Storage
          </div>
          <div className="serviceno1content">
            Our Blockchain Security service provides advanced encryption and
            authentication techniques to safeguard your digital assets and
            transactions.
          </div>
          <div className="serviceno2">
            Secure and Transparent Legal Record Storage{" "}
          </div>
          <div className="serviceno2content">
            Legal eVault is a secure online platform that allows individuals and
            businesses to store and manage their important legal documents.
          </div>
          <div className="serviceno3">
            Secure and Transparent Legal Record Storage
          </div>
          <div className="serviceno3content">
            Record Accessibility provides a secure and efficient way to access
            and manage important records with a formal tone.
          </div>
        </div>
        <div className="footer"></div>
      </div>
    </div>
  );
};

export default LandingPage;
