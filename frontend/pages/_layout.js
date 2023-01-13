import React from "react";
import Footer from "../src/components/Footer";
import Navbar from "../src/components/Navbar";
import { slide as Menu } from "react-burger-menu";

const Layout = ({ children }) => {
  const showSettings = (event) => {
    event.preventDefault();
  };

  return (
    <div>
      <Menu width={200} noOverlay className="font-sans">
        <a id="home" className="menu-item" href="/">
          Home
        </a>
        <a id="cars" className="menu-item" href="/cars">
          Cars
        </a>
        <a onClick={showSettings} className="menu-item--small" href="">
          Settings
        </a>
      </Menu>
      <Navbar />
      {children}
      <Footer />
    </div>
  );
};

export default Layout;
