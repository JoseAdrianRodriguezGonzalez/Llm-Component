# Pipeline Completo con Evaluación de Idioma + Características Literarias, Semánticas y Lógica Difusa

## Objetivo
Evaluar automáticamente lecturas de tarot generadas en inglés y español, midiendo:

- Detección y evaluación del idioma (fluidez, gramática, coherencia)
- Calidad semántica y coherencia con contexto
- Claridad y legibilidad
- Abstracción y uso de lenguaje figurado
- Características poéticas y estilísticas
- Combinación de todas las métricas con lógica difusa para evaluación final flexible

---

## Pipeline General

### 1. Detección y Evaluación del Idioma

- **Detección:** Usar modelos o librerías (p.ej. `fasttext` o `langdetect`) para identificar si el texto está en inglés o español.
- **Evaluación de calidad del idioma:**
  - Comprobar corrección gramatical y sintáctica con modelos de corrección gramatical multilingües (ej: `LanguageTool`, `Grammarly API`, modelos transformer específicos para corrección).
  - Medir fluidez y naturalidad con puntuaciones de probabilidad de lenguaje de modelos de lenguaje grandes (p.ej. perplexity con GPT, GPT-3/4, LLaMA, u otros).
  - Detectar errores comunes: concordancia, tiempos verbales, uso de preposiciones, etc.
  - Resumir calidad del idioma en una puntuación cuantitativa (por ejemplo, porcentaje de oraciones sin errores detectados).

### 2. Preprocesamiento y Normalización

- Limpieza de texto, tokenización y segmentación de oraciones.
- Adaptar procesos según el idioma detectado (ej. tokenización específica de español o inglés).

### 3. Extracción de Representaciones Semánticas

- Obtener embeddings con modelos transformer multilingües (`XLM-RoBERTa`, `mBERT`, `sentence-transformers`).
- Calcular similitud semántica entre lectura generada y contexto para medir coherencia y alineación temática.

### 4. Evaluación de Claridad y Legibilidad

- Usar métricas específicas por idioma:
  - Inglés: Flesch Reading Ease, Gunning Fog.
  - Español: Fernández-Huerta, Szigriszt-Pazos.
- Medir longitud promedio de oraciones, complejidad léxica y ambigüedad.
- Evaluar estructura gramatical y coherencia discursiva.

### 5. Evaluación de Abstracción

- Analizar vocabulario para detectar palabras abstractas, emocionales, simbólicas.
- Detectar uso de metáforas, analogías o lenguaje figurado (usando diccionarios, NLP o modelos entrenados).
- Medir densidad conceptual y subjetividad.

### 6. Evaluación Poética y Estilística

- Análisis de ritmo, métrica aproximada, aliteraciones y rimas.
- Detección de figuras retóricas básicas (anáforas, hipérboles).
- Análisis de tonalidad y emoción mediante análisis de sentimiento contextual.
- Identificar coherencia estilística con lecturas etéreas y simbólicas.

### 7. Combinación con Lógica Difusa

- Definir variables difusas para cada dimensión (idioma, semántica, claridad, abstracción, poesía).
- Crear funciones de membresía específicas para cada métrica, ajustadas por idioma.
- Construir reglas difusas para integrar todas las puntuaciones en un índice global de calidad.
- Permitir evaluación flexible que admita textos parcialmente imperfectos pero con buen estilo.

### 8. Salida y Reportes

- Resultados detallados con puntuaciones por dimensión y evaluación del idioma.
- Sugerencias para mejorar calidad idiomática o estilística.
- Soporte para visualizar comparaciones entre versiones en inglés y español.


## Ejemplo de flujo con énfasis en evaluación de idioma

Entrada de texto →
Detectar idioma →
Evaluar gramática y fluidez (corrección + perplexity) →
Preprocesar texto →
Obtener embeddings y medir similitud semántica →
Evaluar claridad y legibilidad →
Detectar abstracción y metáforas →
Analizar poesía y estilo →
Combinar con lógica difusa →
Output con evaluación detallada incluyendo calidad idiomática