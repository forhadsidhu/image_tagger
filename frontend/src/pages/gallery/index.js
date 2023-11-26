import React ,{ useState }from 'react';
import ImagWorldCard from './card';
import Jumbutron from '../../components/Jumbutron'; 
import SearchField from "../../components/SearchField";
import MultipleImageUpload from './MultipleImageUpload';
import { Modal, ProgressBar, Button } from 'react-bootstrap';

import {
  Nav,
  NavBarContainer,
  NavLogo,
  MobileIcon,
  NavMenu,
  NavItem,
  NavLinks,
  NavBtn,
  NavBtnLink,
  LoginWhite,
  LoginBlack
} from "../../components/NavBar/NavBarElements";
import Footer from "../../components/Footer";
const ImagePage = () => {


  const [showModal, setShowModal] = useState(false);

  const handleButtonClick = () => {
    setShowModal(true); // Toggle the state
  };

  const closeModal = () => {
    setShowModal(false);
  };

  const handleModalExited = () => {
    setShowModal(false); // Reset the modal state when it exits
  };



  // Generate an array of image URLs
  const imageUrls = Array.from({ length: 50 }, (_, index) => `https://picsum.photos/200?random=${index}`);

  // Render the images in rows with 10 images per row
  const renderImageRows = () => {
    const rows = [];
    for (let i = 0; i < imageUrls.length; i += 10) {
      const rowImages = imageUrls.slice(i, i + 10).map((url, index) => (
        <ImagWorldCard key={index} imageUrl={url} title={<span style={{ color: 'black', fontSize: '15px' }}> Sample Image ${i + index + 1}</span>}/>
      ));
      rows.push(<div className="row" key={i}>{rowImages}</div>);
    }
    return rows;
  };




  return (
    <div>

      <Nav>
        <NavBarContainer>
          <NavLogo to="/" >
            <h1>Tagify</h1>
          </NavLogo>
          <NavMenu>
            <NavItem>
              <NavLinks
                to="about"
                smooth={true}
                duration={500}
                spy={true}
                offset={+70}
              >
                <SearchField />
              </NavLinks>
            </NavItem>
          </NavMenu>
        
          <NavBtn>
            <NavBtnLink
              to="#"
              onClick={handleButtonClick}
            >
              Upload
            </NavBtnLink>
          </NavBtn>  
        </NavBarContainer>
      </Nav>


      {/* Modal with larger size */}
      {showModal && (
        <div className="modal-wrapper">
          <div className="modal-overlay" onClick={closeModal}></div>
          <div className="custom-modal">
            <Modal  show={showModal} onHide={closeModal} size="lg" onExited={handleModalExited}>
              <Modal.Header closeButton>
                <Modal.Title>Upload Images</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                <MultipleImageUpload />
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={closeModal}>
                  Close
                </Button>
              </Modal.Footer>
            </Modal>
          </div>
        </div>
      )}

      <div className="card-container">
         {renderImageRows()}
      </div>
      <Footer/>





    </div>
  );
};

export default ImagePage;
