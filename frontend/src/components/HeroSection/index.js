import React, { useState } from "react";
import Video from "../../assets/video/dame_home_page_video.mp4";
import { Button } from "../Buttons/ButtonElement";
import {
  HeroContainer,
  HeroBg,
  VideoBg,
  HeroContent,
  HeroButton,
  HeroP,
  HeroBtnWrapper,
  CurrencyWhite,
  HeroH1,
} from "./HeroElements";
import { Link } from 'react-router-dom';


const HeroSection = () => {
  const [hover, setHover] = useState(false);

  const onHover = () => {
    setHover(hover ? false : true);
  };

  return (
    <HeroContainer>
      <HeroBg>
        <VideoBg autoPlay loop muted src={Video} type="video/mp4" />
      </HeroBg>
      <HeroContent>
        <HeroH1>Welcome to our world!</HeroH1>
        <Link to="/image_world">
          <HeroButton>Enter</HeroButton>
        </Link>
      </HeroContent>
    </HeroContainer>
  );
};

export default HeroSection;
