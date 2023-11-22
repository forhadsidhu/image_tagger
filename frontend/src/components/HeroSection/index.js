import React, { useState } from "react";
import Video from "../../assets/video/dame_home_page_video.mp4";
import { Button } from "../Buttons/ButtonElement";
import {
  HeroContainer,
  HeroBg,
  VideoBg,
  HeroContent,
  HeroH1,
  HeroP,
  HeroBtnWrapper,
  CurrencyWhite,
  CurrencyBlack,
} from "./HeroElements";

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
    </HeroContainer>
  );
};

export default HeroSection;
