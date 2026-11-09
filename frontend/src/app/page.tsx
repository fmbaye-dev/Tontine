'use client'

import { useEffect, useState } from "react";
import api from "./api";
import { Check, MailDot, ArchiveArrowDown } from "lucide-react";

interface Versement {    // modele de versement conformément à la description sur models django
  id: string;
  description: string; 
  montant: number;
  date_versement: string;
}


export default function Home() {
  // TRAITEMENT

  const [versements, setVersement] = useState<Versement[]>([])

  useEffect(() => {
    async function recupVersements() {
      // 1. Récupération de tous les versements avec la méthode get
      const api_access = await api.get<Versement[]>("versements/")     // a. Accès à l'api de tous les versements
      setVersement(api_access.data)                                    // b. consommation
    }
    recupVersements();
  }, [])
  

  const somme_due = 10000

  const total_cotise = versements.reduce((total, v) => {
    if (v.montant > 0) {       // si le montant du versement est positif donc on incrémente la valeur total_cotise
      return total + v.montant
    }
    else {
      return total + v.montant       // si le montant du versement est négatif, on ajoute une valeur négative ce qui revient à décrémenter total cotisé
    }
  }, 0);

  const reste_a_complete = somme_due - total_cotise
  
  return (
    <div className="stats shadow w-3/4 mx-auto p-6">
      {/* VISUALISATION */}
      
        <div className="stat place-items-center">
          <div className="stat-title badge">
            <MailDot /> Somme due</div>
          <div className="stat-value">{somme_due}</div>
        </div>

        <div className="stat place-items-center">
          <div className="stat-title badge">
            <Check /> Total cotisé
          </div>
          <div className="stat-value text-secondary">{total_cotise}</div>
        </div>

        <div className="stat place-items-center">
          <div className="stat-title badge">
            <ArchiveArrowDown />Reste à compléter</div>
          <div className="stat-value">{reste_a_complete}</div>
        </div>
    </div>  
  );
}