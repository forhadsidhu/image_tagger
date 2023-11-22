import React, { useState } from "react";
import NavBar from "../../components/NavBar";
import SideBar from "../../components/SideBar";
import HeroSection from "../../components/HeroSection";
import DataSection from "../../components/DataSection";
import { dataInfo } from "../../components/DataSection/Data";
import Footer from "../../components/Footer";

const Home = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(isOpen ? false : true);
  };

  return (
    <>
      <SideBar isOpen={isOpen} toggle={toggle} />
      <NavBar toggle={toggle} />
      <HeroSection />
      <DataSection {...dataInfo} />
      <Footer />
    </>
  );
};

export default Home;
