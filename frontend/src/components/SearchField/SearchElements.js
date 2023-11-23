
import styled from 'styled-components';

export const SearchContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #000;
  padding: 0px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
`;

export const SearchInput = styled.input`
  padding: 8px;
  border-radius: 5px;
  margin-right: 5px;
  border: none;
  outline: none;
`;

export const SearchButton = styled.button`
  padding: 8px 12px;
  border-radius: 5px;
  border: none;
  outline: none;
  background-color: #333;
  color: #fff;
  cursor: pointer;
`;
