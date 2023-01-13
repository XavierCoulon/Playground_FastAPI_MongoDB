import React from "react";
import axios from "axios";
import Link from "next/link";

function Car({ data }) {
  return (
    <>
      <img className="w-28" src={data.image_brand} alt="picture of a brand" />
      {data.image_model.startsWith("http") ? (
        <img src={data.image_model} alt="picture of a car" />
      ) : (
        <p>No image</p>
      )}

      <ul>
        <li>{data.brand}</li>
        <li>{data.motorisation}</li>
        <li>{data.autonomy}</li>
        <li>{data.price}€</li>
        <li>{data.rating}</li>
      </ul>
      <Link href="/cars">Retour...</Link>
    </>
  );
}

export default Car;

// getServerSideProps or getStaticProps
export const getStaticProps = async ({ params }) => {
  const { data } = await axios.get(
    `http://localhost:8000/api/v1/${params._id}`
  );
  return { props: { data } };
};

export async function getStaticPaths() {
  const { data } = await axios.get("http://localhost:8000/api/v1");
  return {
    paths: data.map((car) => ({
      params: {
        _id: car._id.toString(),
      },
    })),
    fallback: false,
  };
}
