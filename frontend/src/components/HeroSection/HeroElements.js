import styled from "styled-components";
import { RiCurrencyLine, RiCurrencyFill } from "react-icons/ri";

export const HeroContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10 100px;
  height: 800px;
  position: relative;
  z-index: 1;
  border:none;
  border-radius: 20px;
`;

export const HeroBg = styled.div`
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
`;

export const VideoBg = styled.video`
  width: 100%;
  height: 100%;
  -o-object-fit: cover;
  object-fit: cover;
  background: #ffffff;
  filter: brightness(120%); /* Adjust the percentage to increase brightness */
`;

export const HeroContent = styled.div`
  z-index: 5;
  max-width: 1500px;
  position: absolute;
  padding: 8px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  
`;

export const HeroH1 = styled.h1`
  color: #fff;
  font-size: 48px;
  text-align: center;

  @media screen and (max-width: 768px) {
    font-size: 40px;
  }

  @media screen and (max-width: 480px) {
    font-size: 32px;
  }
`;

export const HeroP = styled.p`
  margin-top: 24px;
  color: #fff;
  font-size: 24px;
  text-align: center;
  max-width: 600px;

  @media screen and (max-width: 768px) {
    font-size: 24px;
  }

  @media screen and (max-width: 480px) {
    font-size: 18px;
  }
`;

export const HeroBtnWrapper = styled.div`
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const CurrencyWhite = styled(RiCurrencyLine)`
  margin-left: 8px;
  font-size: 20px;
`;

export const CurrencyBlack = styled(RiCurrencyFill)`
  margin-left: 8px;
  font-size: 20px;
`;


export const HeroButton = styled.button`
    border-radius: 50px;
    background: #F9B81F;
    padding: 10px 100px;
    color: #010606;
    font-size: 20px;
    text-decoration: none;
    border: none;
    outline: none;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s ease-in-out;

    &:hover {
        transition: all 0.2s ease-in-out;
        background: #3b88c3 !important;
        border-color: none;
        color: white;
        outline: none;
        text-decoration: none;
    }
  `;




