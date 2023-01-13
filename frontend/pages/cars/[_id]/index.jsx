import React from "react";
import axios from "axios";
import Link from "next/link";

function Car({ data }) {
  return (
    <>
      <div className="flex justify-center p-4">
        <div className="px-4 ">
          {data.image_model.startsWith("http") ? (
            <img
              className="w-96 rounded-lg"
              src={data.image_model}
              alt="picture of a car"
            />
          ) : (
            <p>No image</p>
          )}
        </div>
        <ul>
          <li>
            <img
              className="w-28 h-auto"
              src={data.image_brand}
              alt="picture of a brand"
            />
          </li>
          <li>{data.brand}</li>
          <li>{data.motorisation}</li>
          <li>{data.autonomy}</li>
          <li>{data.price}€</li>
          <li>{data.rating}</li>
        </ul>
      </div>
      <Link href="/cars" className="bg-blue-400 text-white p-2 ml-1 rounded-md">Retour</Link>

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
