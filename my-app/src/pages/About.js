import React from "react";
import moonpic from "../assets/moon (1) 2.png";
import "./About.css";

const copyContent = async () => {
  try {
    await navigator.clipboard.writeText("admintrustvault@gmail.com");
    document.getElementsByClassName("contact")[0].style.color = "#06f";
    document.getElementsByClassName("contact")[0].innerHTML = "Copied!";
  } catch (err) {
    console.error("Failed to copy: ", err);
  }
};

const handlemouseenter = () => {
  document.getElementsByClassName("contactspan")[0].style.color = "#06f";
};

const handlemouseleave = () => {
  document.getElementsByClassName("contactspan")[0].style.color = "#000";
}

const About = () => {
  return (
    <div>
      <div className="colourmode">
        <img src={moonpic} alt="moon" className="moon"></img>
      </div>
      <div className="head">About</div>
      <div className="sub1">Our Vision</div>
      <div className="para1">
        It is to revolutionize the way legal records are stored and accessed, by
        leveraging the power of blockchain technology. By creating a secure and
        transparent e-Vault system, we aim to provide a seamless experience for
        all stakeholders involved in the legal industry. Our ultimate goal is to
        enhance efficiency, trust, and accessibility in legal record management,
        paving the way for a more streamlined and reliable legal ecosystem.
      </div>
      <div className="talk">Let's talk;</div>
      <div className="contact">
        Contact :{" "}
        <span
          className="contactspan"
          onClick={copyContent}
          onMouseEnter={handlemouseenter}
          onMouseLeave={handlemouseleave}
        >
          admintrustvault@gmail.com
        </span>
      </div>
    </div>
  );
};

export default About;
