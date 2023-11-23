import React from 'react';
import './card.css';

const Card = ({ imageUrl, title }) => {
  return (
    <div className="card">
      <img src={imageUrl} alt={title} />
      <div className="card-content">
        <h3>{title}</h3>
      </div>
    </div>
  );
};

export default Card;
