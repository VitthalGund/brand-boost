import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import BrandBoost from "../components/BrandBoost";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>BrandBoost Pro 🚀 | Elevate Your Branding with Precision and Ease 🎯</title>
        <meta
          name="description"
          content="Generate branding snippets for your product."
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <BrandBoost />
    </div>
  );
};

export default Home;
